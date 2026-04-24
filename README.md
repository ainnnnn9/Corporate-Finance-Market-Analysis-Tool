# Corporate Financial and Markets Analysis Tool

## 1. Problem & User
Individual investors and financial analysts often face a "data gap" where retail market prices are disconnected from academic-grade corporate financial metrics. This tool provides an **Institutional-grade Research Terminal** for equity analysts and corporate finance students to bridge this gap, using verified **WRDS** database sources for robust valuation and risk assessment.

## 2. Data
* **Primary Source:** **Wharton Research Data Services (WRDS)** – Accessing the **CRSP** (Center for Research in Security Prices) daily stock files.
* **Access Date:** April 2026.
* **Key Fields:** * `ticker`: Stock identifier.
    * `date`: Trading timestamp.
    * `prc`: Closing price (handled for bid-ask averages).
    * `permno`: Security permanent identifier for cross-sectional consistency.

## 3. Methods
The application follows a professional data pipeline:
* **Authentication:** Established a secure tunnel to WRDS with built-in **Session Rollback** logic to ensure connection stability and prevent transaction deadlocks.
* **Extraction:** Utilized dynamic **SQL queries** to fetch cross-sectional market data based on user-defined tickers and timeframes.
* **Data Engineering:** Processed raw datasets by handling non-trading quote flags (converting negative CRSP prices to absolute values) and deduplicating records caused by historical corporate name changes.
* **Quantitative Analytics:** Implemented rolling volatility, exponential moving averages (50D/200D), and **Maximum Drawdown** stress testing.

## 4. Key Findings
* **Momentum Identification:** By visualizing the crossover of 50-day and 200-day moving averages, the tool effectively identifies structural bullish or bearish trends.
* **Risk Quantization:** The **Maximum Drawdown** analysis provides a clear view of historical capital risk, helping users understand "worst-case" scenarios for specific assets.
* **Portfolio Efficiency:** Through the Risk vs. Return scatter plot, the tool demonstrates how different assets align along the capital market line.
* **Automated Decision Support:** The **Analyst Insights** engine categorizes assets into *Outperform*, *Neutral*, or *Speculative* based on objective quantitative thresholds (Return vs. Volatility).

## 5. How to Run
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[Your-Username]/[Your-Repo-Name].git
    ```
2.  **Install Dependencies:**
    ```bash
    pip install streamlit pandas wrds plotly
    ```
3.  **Run the Application:**
    ```bash
    streamlit run app.py
    ```
4.  **Important Note:** When the app starts, check your **Terminal/Command Prompt**. You will be prompted to enter your **WRDS username and password** to establish the database connection.

## 6. Product Link / Demo
* **Demo Video:** [Insert Link Here]
* **GitHub Repository:** [Insert Link Here]

## 7. Limitations & Next Steps
* **Data Latency:** Currently utilizes CRSP daily files, which typically have a multi-month lag compared to real-time market feeds, suitable for mid-to-long term research.
* **Fundamental Integration:** Future phases involve integrating **Compustat** data to automate bottom-up fundamental analysis (e.g., ROE, Net Margin, and Debt-to-Equity ratios).
* **Portfolio Optimization:** Implementation of Mean-Variance Optimization (MVO) to suggest mathematically efficient asset allocations.

---
**Institutional Data Source:** WRDS CRSP | **Developed for:** Corporate Finance & Market Research Analysis
