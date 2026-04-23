# Corporate Finance & Market Analysis Tool

## 1. Problem & User
This project helps finance and accounting students understand whether a stock’s performance is driven by firm-specific factors or broader market movements.

## 2. Data
- WRDS (Wharton Research Data Services)
- Yahoo Finance API  
Access date: April 2026  

Key fields:
- Closing prices
- Returns
- Market index data

## 3. Methods
- Data collection using Python APIs
- Data cleaning and transformation
- Moving averages (trend analysis)
- Volatility (risk measurement)
- Drawdown (downside risk)
- Correlation and benchmarking
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

## 6. Product Link / Demo
[Insert Streamlit or GitHub link]

## 7. Limitations & Next Steps
-Yahoo Finance data may be inconsistent
-Limited WRDS integration
-No predictive modelling

Future improvements:
-Portfolio optimization
-Fundamental analysis
-Enhanced WRDS usage
