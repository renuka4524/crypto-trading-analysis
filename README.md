# 📊 Bitcoin Sentiment Analysis

A data analysis project exploring the relationship between crypto market sentiment and trading performance over a 22-month period (Jul 2023 – Apr 2025).

## 🔍 Overview

This project analyses Bitcoin trading data combined with Fear & Greed sentiment data to uncover patterns between market sentiment and trader profitability.

## 📁 Project Structure

```
crypto-trading-analysis/
├── Bitcoin_sentiment_analysis.py   # Main analysis script
├── fear_greed.csv                  # Fear & Greed sentiment data
├── historical_data.csv             # Historical trading data
└── Charts/                         # Generated visualisations
```

## 📌 Analysis Phases

- **Phase 1** — Data loading and exploration
- **Phase 2** — Data cleaning and preprocessing
- **Phase 3** — Sentiment distribution analysis
- **Phase 4** — PnL vs Sentiment correlation
- **Phase 5** — Top trader performance analysis
- **Phase 6** — Monthly PnL trend and final insights

## 📈 Key Findings

- Top trader earned **$2.14M** in closed PnL over the period
- Top 10 traders combined earned over **$10.6M**
- A major market crash in **August 2024** pushed average PnL negative (~-$75)
- Market recovered and stabilised at **$35–60 avg PnL** through early 2025
- Negative sentiment periods closely aligned with low/negative PnL months

## 🛠️ Libraries Used

```python
pandas
matplotlib
seaborn
numpy
```

## 🚀 How to Run

1. Clone this repository
2. Install dependencies: `pip install pandas matplotlib seaborn numpy`
3. Run the script: `python Bitcoin_sentiment_analysis.py`

## 👩‍💻 Author

**Renuka** — [github.com/renuka4524](https://github.com/renuka4524)
