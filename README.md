# Corporate Financial and Markets Analysis Tool

## 🔗 Product Link

(Local Streamlit App – demonstrated via CMD execution)


## 1. Problem & User

This project is designed for accounting students who want to understand how market data reflects company performance and financial risk.
Traditional accounting focuses on financial statements, but lacks real-time market insights.


## 2. Data

* Source: WRDS CRSP database
* Access Date: 2026
* Key Fields:

  * `date` (trading date)
  * `prc` (stock price)
  * `ticker` (company identifier)


## 3. Methods (Cleaning, Transformation & Analysis)

### Data Cleaning

* Removed duplicate records from CRSP joins
* Converted negative price values to absolute values (CRSP convention)
* Standardised date format using pandas

### Data Transformation

* Sorted data by ticker and time
* Created rolling indicators:

  * 50-day Moving Average (short-term trend)
  * 200-day Moving Average (long-term trend)
* Calculated:

  * Returns (percentage change)
  * Volatility (annualised standard deviation)
  * Maximum Drawdown (peak-to-trough decline)

### Metrics & Comparisons

* Multi-company comparison (AAPL vs MSFT etc.)
* Risk comparison using drawdown
* Performance comparison using total return
* Automated rating system (Outperform / Market / High Speculation)


## 4. Key Findings

* Moving averages clearly reveal trend direction over different horizons
* Maximum drawdown highlights downside risk during market stress
* Different companies exhibit different volatility-risk profiles
* Automated insights simplify interpretation for non-finance users


## 5. How to Run (Local Execution via CMD)

1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   streamlit run app.py

3. Enter WRDS username and password when prompted


## 6. Demo

* Demo Video: (insert link)


## 7. Limitations & Next Steps

* Financial ratios are simplified and not dynamically retrieved
* Requires WRDS access (limits general usability)
* Future improvements:

  * Integrate real financial statement data
  * Expand financial indicators
  * Improve UI and usability
