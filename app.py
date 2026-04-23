import streamlit as st
import pandas as pd
import wrds
import plotly.graph_objects as go
from datetime import datetime

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="WRDS Finance Tool", layout="wide")
st.title("📊 WRDS Corporate Finance Analysis Tool")

st.markdown("""
This tool uses **WRDS academic database** to analyze stock performance, risk, and market behavior.
It focuses on **trend, volatility, drawdown, and cross-market comparison**.
""")

# =========================
# WRDS CONNECTION (cached)
# =========================
@st.cache_resource
def get_wrds_connection():
    try:
        db = wrds.Connection()
        return db
    except Exception as e:
        return None

db = get_wrds_connection()

if db is None:
    st.error("WRDS connection failed. Please check deployment environment.")
    st.stop()

# =========================
# INPUT
# =========================
tickers = st.multiselect(
    "Select Stocks",
    ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"],
    default=["AAPL"]
)

years = st.slider("Years of Data", 1, 5, 2)

# =========================
# FETCH FROM WRDS (CRSP style simulation)
# =========================
@st.cache_data
def fetch_data(symbol):
    try:
        # NOTE: real WRDS CRSP query (simplified template)
        query = f"""
        SELECT date, prc AS close
        FROM crsp.dsf
        WHERE permno IN (
            SELECT permno FROM crsp.stocknames WHERE ticker = '{symbol}'
        )
        AND date >= current_date - interval '{years} years'
        """

        df = db.raw_sql(query)

        if df is None or df.empty:
            return None

        df['date'] = pd.to_datetime(df['date'])
        df = df.set_index('date')
        df = df.sort_index()

        return df

    except:
        return None

# =========================
# LOAD DATA
# =========================
data = {}

for t in tickers:
    df = fetch_data(t)
    if df is not None and not df.empty:
        data[t] = df
    else:
        st.warning(f"{t} data not found in WRDS")

if len(data) == 0:
    st.error("No valid WRDS data loaded")
    st.stop()

# =========================
# PRICE TREND
# =========================
st.subheader("📈 Price Trend")

fig = go.Figure()

for t, df in data.items():
    fig.add_trace(go.Scatter(
        x=df.index,
        y=df['close'],
        name=t
    ))

fig.update_layout(template="plotly_white")
st.plotly_chart(fig, use_container_width=True, key="price")

# =========================
# RETURNS
# =========================
st.subheader("📊 Returns Comparison")

fig2 = go.Figure()

for t, df in data.items():
    norm = (df['close'] / df['close'].iloc[0]) * 100
    fig2.add_trace(go.Scatter(x=df.index, y=norm, name=t))

fig2.update_layout(template="plotly_white")
st.plotly_chart(fig2, use_container_width=True, key="returns")

# =========================
# VOLATILITY
# =========================
st.subheader("🛡️ Volatility")

fig3 = go.Figure()

for t, df in data.items():
    returns = df['close'].pct_change()
    vol = returns.rolling(21).std() * (252 ** 0.5)
    fig3.add_trace(go.Scatter(x=df.index, y=vol, name=t))

fig3.update_layout(template="plotly_white")
st.plotly_chart(fig3, use_container_width=True, key="vol")

# =========================
# DRAW DOWN
# =========================
st.subheader("📉 Drawdown")

fig4 = go.Figure()

for t, df in data.items():
    roll_max = df['close'].cummax()
    dd = (df['close'] - roll_max) / roll_max
    fig4.add_trace(go.Scatter(x=df.index, y=dd, name=t))

fig4.update_layout(template="plotly_white")
st.plotly_chart(fig4, use_container_width=True, key="dd")

# =========================
# INSIGHTS
# =========================
st.subheader("📑 Insights")

for t, df in data.items():
    latest = df['close'].iloc[-1]
    mean = df['close'].mean()

    if latest > mean:
        st.success(f"{t}: Above long-term average (bullish bias)")
    else:
        st.warning(f"{t}: Below long-term average (weak trend)")

st.caption(f"WRDS powered analysis | Generated {datetime.now().date()}")
