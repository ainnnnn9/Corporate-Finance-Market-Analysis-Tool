import streamlit as st
import pandas as pd
import wrds
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, date

# ==========================================
# 1. PAGE CONFIG
# ==========================================
st.set_page_config(page_title="Corporate Finance Analysis Tool", layout="wide")
st.title("📊 Corporate Finance & Market Analysis Tool")

# ==========================================
# 2. WRDS CONNECTION (Self-Healing)
# ==========================================
@st.cache_resource
def get_wrds_connection():
    try:
        return wrds.Connection()
    except Exception as e:
        return None

db = get_wrds_connection()

if db is None:
    st.error("❌ WRDS Connection Failed. Check your terminal for password prompt.")
    st.stop()

# ==========================================
# 3. SIDEBAR (Universal Ticker Input)
# ==========================================
st.sidebar.header("🛠️ Parameters")
ticker_input = st.sidebar.text_input("Enter Ticker Symbols (e.g. AAPL, NVDA, MSFT)", "AAPL, MSFT")
selected_tickers = [x.strip().upper() for x in ticker_input.split(",") if x.strip()]

today = date.today()
start_default = today.replace(year=today.year - 2)
date_range = st.sidebar.date_input("Timeframe", [start_default, today])

# ==========================================
# 4. ROBUST DATA FETCHING (Fixing the Rollback Error)
# ==========================================
@st.cache_data
def fetch_wrds_data(tickers, start_date):
    if not tickers:
        return pd.DataFrame()
        
    ticker_str = "','".join(tickers)
    
    # 核心修复点：每次查询前先强制清理之前的死锁状态
    try:
        db.raw_sql("ROLLBACK") 
    except:
        pass
        
    # 最简查询语句，确保兼容性
    query = f"""
    SELECT a.date, a.prc, b.ticker
    FROM crsp.dsf AS a
    JOIN crsp.stocknames AS b ON a.permno = b.permno
    WHERE b.ticker IN ('{ticker_str}')
    AND a.date >= '{start_date}'
    """
    
    try:
        df = db.raw_sql(query)
        if df is not None and not df.empty:
            # 去除由于 CRSP 历史更名产生的重复项
            df = df.drop_duplicates(subset=['date', 'ticker'])
            df['date'] = pd.to_datetime(df['date'])
            df['prc'] = df['prc'].abs() # CRSP 负值处理
            return df.sort_values(['ticker', 'date'])
        return pd.DataFrame()
    except Exception as e:
        # 如果依然报错，尝试强制重新初始化引擎
        st.error(f"Database Session Error: {e}")
        return pd.DataFrame()

# Run Data Engine
if len(selected_tickers) > 0 and len(date_range) == 2:
    raw_df = fetch_wrds_data(selected_tickers, date_range[0])
else:
    st.stop()

# ==========================================
# 5. ERROR HANDLING & ANALYSIS
# ==========================================
if raw_df.empty:
    st.warning("⚠️ No data returned. Possible reasons: \n1. Ticker is wrong. \n2. Date range is too short. \n3. Connection issue.")
    # 提供一个重试按钮来清理缓存
    if st.button("Clear Cache & Retry"):
        st.cache_data.clear()
        st.rerun()
    st.stop()

# --- ANALYTICAL TABS ---
tab1, tab2, tab3 = st.tabs(["📈 Performance", "🛡️ Risk Metrics", "🎯 Portfolio Efficiency"])

with tab1:
    main_t = selected_tickers[0]
    main_df = raw_df[raw_df['ticker'] == main_t].copy()
    if not main_df.empty:
        st.subheader(f"Analysis: {main_t}")
        main_df['MA50'] = main_df['prc'].rolling(50).mean()
        main_df['MA200'] = main_df['prc'].rolling(200).mean()
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=main_df['date'], y=main_df['prc'], name="Close Price"))
        fig.add_trace(go.Scatter(x=main_df['date'], y=main_df['MA50'], name="50D MA", line=dict(dash='dot')))
        fig.add_trace(go.Scatter(x=main_df['date'], y=main_df['MA200'], name="200D MA", line=dict(width=2)))
        fig.update_layout(template="plotly_white", margin=dict(l=0,r=0,t=20,b=0))
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.subheader("Maximum Drawdown (Historical Risk)")
    fig_dd = go.Figure()
    for t in selected_tickers:
        t_df = raw_df[raw_df['ticker'] == t].copy()
        if not t_df.empty:
            t_df['dd'] = (t_df['prc'] - t_df['prc'].cummax()) / t_df['prc'].cummax()
            fig_dd.add_trace(go.Scatter(x=t_df['date'], y=t_df['dd'], name=t, fill='tozeroy'))
    fig_dd.update_layout(template="plotly_white", yaxis_tickformat='.1%')
    st.plotly_chart(fig_dd, use_container_width=True)

with tab3:
    st.subheader("Risk vs. Return Portfolio Efficiency")
    stats = []
    for t in selected_tickers:
        t_df = raw_df[raw_df['ticker'] == t]
        rets = t_df['prc'].pct_change().dropna()
        if not rets.empty:
            stats.append({'Ticker': t, 'Return': rets.mean()*252, 'Vol': rets.std()*(252**0.5)})
    if stats:
        sdf = pd.DataFrame(stats)
        fig_s = px.scatter(sdf, x="Vol", y="Return", text="Ticker", size_max=15, template="plotly_white")
        fig_s.update_traces(textposition='top center', marker=dict(size=12))
        st.plotly_chart(fig_s, use_container_width=True)
