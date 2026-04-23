# Corporate Finance & Market Analysis Tool

## 1. Problem & User
This project helps finance and accounting students understand whether a stock’s performance is driven by firm-specific factors or broader market movements.

## 2. Data
- **Source:** WRDS (Wharton Research Data Services), Yahoo Finance API
- **Access Date:** April 2026

**Key Fields:**
- Closing prices
- Daily returns
- Market index data

## 3. Methods
- Data collection using Python APIs
- Data cleaning and transformation
- Moving averages (trend analysis)
- Volatility (risk measurement)
- Drawdown (downside risk)
- Benchmark comparison and correlation
- Visualization using Plotly

## 4. Key Findings
- High correlation indicates strong market-driven behavior
- Volatility varies across companies
- Some stocks outperform benchmarks consistently
- Drawdown reveals hidden downside risks
- Risk-return trade-offs differ across assets

## 5. How to Run
```bash
pip install streamlit yfinance wrds plotly pandas
streamlit run app.py
```

## 6. Product Link / Demo
- **Live App:** https://your-streamlit-link-here
- **GitHub Repository:** https://github.com/your-username/your-repo
- **Demo Video:** https://your-video-link-here

## 7. Limitations & Next Steps

**Limitations:**
- Yahoo Finance data may be inconsistent
- Limited WRDS integration
- No predictive modelling

**Future Improvements:**
- Portfolio optimization
- Fundamental analysis integration
- Enhanced WRDS data usage
