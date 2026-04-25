# 📊 Corporate Finance & Market Analysis Tool

## 🔗 Product Demo (Local Streamlit App)

Run locally using:

    streamlit run app.py


## 1. Problem & User

This project is designed for accounting and finance students who want to understand how company performance is reflected in market data.

Instead of focusing on trading decisions, the tool provides analytical insights into trend, risk, and market relationships.


## 2. Data

- Source:
  - WRDS (Wharton Research Data Services)
  - Yahoo Finance (via yfinance API)

- Access Date:
  - April 2026

- Key Fields:
  - Close Price
  - Daily Returns
  - Moving Averages (50-day, 200-day)


## 3. Methods

The main Python workflow includes:

- Data retrieval using yfinance  
- Data cleaning:
  - Handling missing values  
  - Flattening multi-index columns  
- Feature engineering:
  - Moving averages (MA50, MA200)  
  - Daily returns  
  - Rolling volatility (21-day)  
- Data transformation:
  - Normalization (Base 100 for comparison)  
- Analysis:
  - Trend analysis (price vs MA200)  
  - Risk measurement (volatility)  
  - Correlation with market benchmark  


## 4. Key Findings

- Moving averages help identify short-term and long-term trends  
- Volatility reflects the risk level of a stock  
- Market benchmarks provide a reference for comparison  
- Correlation indicates how much a stock is driven by market movements  
- Normalized comparison allows cross-market performance evaluation  


## 5. How to Run

1. Install required packages:

    pip install -r requirements.txt

2. Run the app:

    streamlit run app.py

3. Enter:
- WRDS username (password via terminal)  
- Stock ticker (e.g. AAPL)  
- Benchmark and time period  


## 6. Product & Demo

- Local Streamlit interactive app  
- Demo video included in submission  


## 7. Limitations & Next Steps

### Limitations:
- Yahoo Finance API may be unstable  
- WRDS requires manual login  
- Limited financial indicators  

### Next Steps:
- Integrate full WRDS datasets (e.g. CRSP)  
- Add financial statement metrics  
- Improve UI/UX design  
- Enable cloud deployment  
