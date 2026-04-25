# Corporate Financial and Markets Analysis Tool

## 1. Problem & User

This project is designed for accounting students who want to understand how market data reflects company performance and financial risk.

## 2. Data

* Source: WRDS CRSP database (stock price data)
* Access Date: 2026
* Key Fields: date, price (prc), ticker

## 3. Methods

* SQL queries to extract stock data from WRDS
* Data cleaning and processing using pandas
* Calculation of:

  * Moving averages (MA50, MA200)
  * Volatility and returns
  * Maximum drawdown
* Visualization using Plotly
* Interactive interface using Streamlit

## 4. Key Findings

* Stock price trends can be clearly identified using moving averages
* Maximum drawdown highlights risk exposure during market downturns
* Different companies show varying levels of volatility and performance
* Automated insights provide quick interpretation of financial behavior

## 5. How to Run

1. Install required packages:
   pip install -r requirements.txt

2. Run the application:
   streamlit run app.py

3. Enter WRDS username and password to access data

## 6. Product Link / Demo

* Streamlit App: (optional)
* Demo Video: (insert link)

## 7. Limitations & Next Steps

* Some financial ratios are simplified and not dynamically retrieved
* WRDS access is required, which may limit usability
* Future improvements:

  * Integrate real financial statement data
  * Add more advanced financial indicators
  * Improve UI/UX design
