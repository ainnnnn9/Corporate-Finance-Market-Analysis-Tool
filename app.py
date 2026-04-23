import streamlit as st
import pandas as pd
import wrds
import yfinance as yf
import plotly.graph_objects as go
from datetime import datetime, timedelta

# --- Page Config ---
st.set_page_config(page_title="Corporate Finance Insight Tool", layout="wide")

st.title("📊 Corporate Finance & Market Analysis Tool")

st.markdown("""
This tool helps users evaluate whether stock performance is driven by firm-specific factors or market-wide movements.
It provides insights into **trend, risk, drawdown, and risk-return trade-offs**.
""")

# --- WRDS Login ---
st.sidebar.header("🔐 WRDS Login")
username = st.sidebar.text_input("WRDS Username")

@st.cache_resource
def connect_wrds(user):
    if not user:
        return None
    try:
        db = wrds.Connection(wrds_username=user)
        return db
    except:
        return None

db = connect_wrds(username)

if not db:
    st.info("👈 Enter WRDS username (password via terminal)")
    st.stop()

# --- Inputs ---
st.subheader("⚙️ Input Parameters")

col1, col2, col3 = st.columns(3)

with col1:
    tickers = st.multiselect(
        "Select Companies",
        ["AAPL", "MSFT", "GOOG", "AMZN", "TSLA"],
        default=["AAPL"]
    )

with col2:
    bench_dict = {
        "S&P 500 (US)": "^GSPC",
        "Hang Seng (HK)": "^HSI",
        "FTSE 100 (UK)": "^FTSE",
        "Nikkei 225 (JP)": "^N225"
    }
    bench_name = st.selectbox("Benchmark", list(bench_dict.keys()))
    benchmark = bench_dict[bench_name]

with col3:
    years = st.slider("Years", 1, 5, 2)

# --- Data Fetch ---
@st.cache_data
def fetch(symbol, years):
    start = datetime.now() - timedelta(days=years*365)
    df = yf.download(symbol, start=start)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    return df

data = {t: fetch(t, years) for t in tickers}
bench_data = fetch(benchmark, years)

if any(df.empty for df in data.values()) or bench_data.empty:
    st.error("Data error")
    st.stop()

# --- Price Trend ---
st.subheader("📈 Price Trend & Moving Average")

fig = go.Figure()

for t, df in data.items():
    df['MA50'] = df['Close'].rolling(50).mean()
    df['MA200'] = df['Close'].rolling(200).mean()

    fig.add_trace(go.Scatter(x=df.index, y=df['Close'], name=f"{t} Price"))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA50'], name=f"{t} MA50", line=dict(dash='dash')))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA200'], name=f"{t} MA200"))

fig.update_layout(template="plotly_white")
st.plotly_chart(fig, use_container_width=True)

# --- Volatility ---
st.subheader("🛡️ Volatility (Risk)")

fig_vol = go.Figure()

for t, df in data.items():
    returns = df['Close'].pct_change()
    vol = returns.rolling(21).std() * (252**0.5)
    fig_vol.add_trace(go.Scatter(x=df.index, y=vol, name=t))

fig_vol.update_layout(template="plotly_white")
st.plotly_chart(fig_vol, use_container_width=True)

# --- Cumulative Return ---
st.subheader("📊 Cumulative Return Comparison")

fig_ret = go.Figure()

for t, df in data.items():
    norm = (df['Close'] / df['Close'].iloc[0]) * 100
    fig_ret.add_trace(go.Scatter(x=df.index, y=norm, name=t))

bench_norm = (bench_data['Close'] / bench_data['Close'].iloc[0]) * 100
fig_ret.add_trace(go.Scatter(x=bench_data.index, y=bench_norm, name="Benchmark"))

fig_ret.update_layout(template="plotly_white")
st.plotly_chart(fig_ret, use_container_width=True)

# --- Drawdown ---
st.subheader("📉 Maximum Drawdown")

fig_dd = go.Figure()

for t, df in data.items():
    roll_max = df['Close'].cummax()
    drawdown = (df['Close'] - roll_max) / roll_max
    fig_dd.add_trace(go.Scatter(x=df.index, y=drawdown, name=t))

fig_dd.update_layout(template="plotly_white")
st.plotly_chart(fig_dd, use_container_width=True)

# --- Risk vs Return ---
st.subheader("⚖️ Risk vs Return")

risk = []
ret = []
labels = []

for t, df in data.items():
    r = df['Close'].pct_change().dropna()

    ann_return = (df['Close'].iloc[-1] / df['Close'].iloc[0])**(252/len(df)) - 1
    ann_vol = r.std() * (252**0.5)

    risk.append(ann_vol)
    ret.append(ann_return)
    labels.append(t)

fig_scatter = go.Figure()

fig_scatter.add_trace(go.Scatter(
    x=risk,
    y=ret,
    mode='markers+text',
    text=labels,
    textposition="top center"
))

fig_scatter.update_layout(
    xaxis_title="Risk",
    yaxis_title="Return",
    template="plotly_white"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# --- Analysis ---
st.subheader("📑 Automated Insights")

for t, df in data.items():
    current = df['Close'].iloc[-1]
    ma200 = df['MA200'].iloc[-1]

    if current > ma200:
        st.success(f"{t}: Bullish trend")
    else:
        st.warning(f"{t}: Bearish trend")

st.caption(f"Data source: WRDS & Yahoo Finance | {datetime.now().date()}")