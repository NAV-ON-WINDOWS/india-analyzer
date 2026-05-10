# India Beyond Headlines

> How topics trend across 22 years in the Indian news.

A data analysis web app that lets you compare how often any two topics appeared in Indian news headlines between 2001 and 2023 — across 3.8 million real headlines.

---

## Live Demo

🔗 [india-beyond-headlines.streamlit.app](https://india-beyond-headlines.streamlit.app)

---

## What It Does

Type any two topics — `education` and `employment`, `cricket` and `football`, `gold` and `petrol` — and the app analyzes 3.8 million headlines to show you how their media coverage compares year by year, plotted as a dual-axis line graph.

---

## Findings

The default comparison — Education vs Employment — reveals something uncomfortable:

- **Education** peaked at **1,086 headlines in 2012**, coinciding with national debate around the Right to Education Act.
- **Employment** never crossed **112 headlines** in any single year across 22 years — despite unemployment being one of India's most pressing issues.
- Both topics follow a near-identical trend throughout, until **2018**, where coverage of both drops sharply and never recovers to previous levels.

---

## Dataset

- **Source:** [India News Headlines — Kaggle](https://www.kaggle.com/datasets/therohk/india-headlines-news-dataset)
- **Size:** 3,876,557 headlines
- **Columns:** `publish_date`, `headline_category`, `headline_text`
- **Period:** January 2001 — mid 2023
- **Null values:** None

> The dataset is included as `dataset.zip`. Extract `india-news-headlines.csv` into the project root before running locally.

---

## How to Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/NAV-ON-WINDOWS/india-analyzer.git
cd india-analyzer
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Extract the dataset**

Unzip `dataset.zip` in the project root so `india-news-headlines.csv` is present.

**4. Run the app**
```bash
streamlit run app.py
```

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.14 | Core language |
| Pandas | Data loading, filtering, analysis |
| Matplotlib | Dual axis visualization |
| Streamlit | Web app interface |

---

## What I Learned

Built while learning Pandas and Matplotlib from scratch as a first year CS student.

- Reading and validating large CSV files with Pandas
- Boolean masking and conditional filtering across 3.8M rows
- String operations on dataframe columns
- Value counts and year-wise aggregation
- Dual-axis line plotting with peak annotations
- Building and deploying a data web app with Streamlit

---

## Project Structure

```
india-analyzer/
├── app.py              # Streamlit web interface
├── main.py             # Data analysis and plotting logic
├── dataset.zip         # Compressed dataset (93MB)
├── requirements.txt    # Python dependencies
└── README.md           # You are here
```

---

## Author

Built by [Arnav](https://github.com/NAV-ON-WINDOWS) — CS fresher, first data project.  
If you found this interesting, star the repo.
