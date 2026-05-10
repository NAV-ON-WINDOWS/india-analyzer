# India Beyond Headlines

> How topics trend across 22 years in the Indian news.
> Built in a day — learning Streamlit from scratch, integrating a 3.8 million row dataset, and deploying it live. All in one sitting.

A data analysis web app that lets you compare how often any two topics appeared in Indian news headlines between 2001 and 2023, across 3.8 million real headlines.

---

## Live Demo

🔗 [india-beyond-headlines.streamlit.app](https://india-beyond-headlines.streamlit.app)

---

## What It Does

Type any two topics that you want to compare — `education` and `employment`, `cricket` and `football`, `economy` and `inflation` — and the app analyzes 3.8 million headlines to show you how their media coverage compares year by year, plotted as a dual-axis line graph while handelling any discrepancies in the input.

---

## Findings / Interesting Comparisons to Try

| Topic 1 | Topic 2 | What you might find |
|---------|---------|-------------------|
| education | employment | A 10x gap that never closes |
| cricket | football | How India's sporting identity shifted |
| gold | petrol | Two commodities, one economic story |
| modi | gandhi | The changing face of Indian politics |
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
| Zipfile | Unzipping and reading dataset in local environment |

---

## What I Learned

Built on my first Data Analysis project (https://github.com/NAV-ON-WINDOWS/india-unf) where you could only see for yourself how 'Education' and 'Employment' trends in the given time period, here you can actually compare any two factors you wish and that too with an interactive GUI!
Being built in a only one day, I faced through multiple issues and a fast learning phase, but what I learnt was much more comforting than the stress of building it:

- Reading and validating large CSV files with zipfile
- Boolean masking and conditional filtering across 3.8M rows using Pandas
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