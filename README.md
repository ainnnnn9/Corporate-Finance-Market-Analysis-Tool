# 📊 Corporate Finance & Market Analysis Tool

## 🔗 Product Demo (Local Streamlit App)

Run locally using:

    streamlit run app.py


## 1. Problem & User

This project is designed for accounting and finance students who want to understand how company performance is reflected in market data.

Instead of focusing on trading decisions, the tool provides analytical insights into trend, risk, and market relationships.


## 2. Data

* **Primary Source:** WRDS CRSP (Center for Research in Security Prices) database.
* **Access Date:** April 2026 (Live API Retrieval).
* **Key Fields:**
    * `date`: Trading day timestamp for time-series alignment.
    * `prc`: Daily closing price (adjusted for CRSP bid-ask average conventions).
    * `ticker`: Unique stock identifier used for multi-asset cross-referencing.

## 3. Methods 

### 🧹 Data Cleaning
* **Join Optimization:** Eliminated duplicate records generated during the SQL merging of `dsf` and `stocknames` tables.
* **Price Correction:** Systematically converted negative price values into absolute values to ensure analytical accuracy (per CRSP data standards).
* **Standardization:** Implemented `pandas` to normalize timestamps and handle missing trading periods.

### 🔄 Data Transformation
* **Structural Sorting:** Organized the primary dataframe by `ticker` and `date` to facilitate rolling calculations.
* **Moving Averages:** Developed 50-day (short-term) and 200-day (long-term) rolling indicators to identify market momentum.
* **Quantitative Analytics:** * **Returns:** Calculated percentage changes to measure asset growth.
    * **Volatility:** Computed annualized standard deviation to quantify price uncertainty.
    * **Max Drawdown:** Measured the peak-to-trough decline to assess capital preservation risk.

### 📊 Metrics & Comparisons
* **Comparative Benchmarking:** Enabled side-by-side analysis for major equities (e.g., AAPL vs. MSFT).
* **Risk Evaluation:** Visualized downside exposure through integrated drawdown charts.
* **Automated Rating System:** Built a logic-driven engine that assigns *Outperform*, *Market Perform*, or *High Speculation* ratings based on the Risk-Return profile.

## 4. Key Findings

* **Trend Signaling:** Moving average crossovers effectively highlight entry and exit windows for long-term investors.
* **Stress Insights:** Maximum drawdown metrics provide a clearer picture of historical downside risk than simple volatility measures.
* **Asset Heterogeneity:** The tool reveals that market-leading tech companies often exhibit vastly different risk profiles despite similar price trends.
* **Research Efficiency:** Automated insights allow researchers to skip manual calculations and move straight to strategic interpretation.

## 5. How to Run (Local Execution via CMD)

1.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Launch the Application:**
    ```bash
    streamlit run app.py
    ```
3.  **Authentication:** Enter your WRDS credentials in the sidebar to establish the secure database tunnel.

## 6. Demonstration
* **Video Demo:** https://www.bilibili.com/video/BV1JwoRBfEuZ/?vd_source=f4e40d43bb4f08b83c086b7dcc8976e6
* **Local Deployment:** This application is optimized for local workstation execution to ensure maximum data retrieval speeds and stable encrypted tunneling with the WRDS cluster.

## 7. Limitations & Next Steps

### Current Limitations
* **Data Latency:** Dependent on the update cycles of CRSP daily files, which are not suitable for high-frequency trading.
* **Simplified Ratios:** Accounting indicators are currently synthesized for demonstration and not yet dynamically pulled from SEC filings.
* **Subscription Required:** The application requires valid WRDS credentials, limiting its use to academic and institutional environments.

### Future Improvements
* **Dynamic Fundamentals:** Integrate the Compustat database to automate the retrieval of real-time Balance Sheets and Income Statements.
* **ESG Integration:** Incorporate Biodiversity Risk and corporate governance metrics to align with modern sustainable investment research.
* **Portfolio Optimization:** Implement Mean-Variance Optimization to suggest mathematically efficient asset allocations.
* **Advanced UI:** Develop a responsive research dashboard to support multi-asset cross-comparisons and mobile viewing.
