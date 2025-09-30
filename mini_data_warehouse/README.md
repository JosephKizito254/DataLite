# DataLite Project

## Overview

DataLite is a fully functional, lightweight mini data warehouse built with Python, SQLite, Pandas, and Dash. It demonstrates a complete ETL (Extract, Transform, Load) pipeline with an interactive dashboard for analytics. Designed to run efficiently on a standard laptop (Core i3, 4GB RAM), it serves as a foundation for modern data-driven decision-making in businesses and personal projects.

The project provides practical exposure to the skills required for modern data engineering, analytics, and business intelligence workflows, and is future-ready for integration with cloud-based warehouses and AI-driven analytics.

---

## Folder Structure

```
DataLite/
│
├── data/
│   └── sales.csv            # Sample sales data
├── db/
│   └── warehouse.db         # SQLite database (auto-created)
├── etl/
│   ├── extract.py           # Extracts data from CSV
│   ├── transform.py         # Cleans and transforms data
│   └── load.py              # Loads data into SQLite
├── dashboards/
│   └── app.py               # Interactive Plotly Dash dashboard
├── utils/
│   └── scheduler.py         # Automates ETL on a schedule
├── run_etl.py               # Executes the full ETL pipeline
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## Setup Instructions

### 1. Clone the Repository

```powershell
git clone <your-repo-url>
cd DataLite
```

### 2. Create and Activate Virtual Environment

```powershell
python -m venv venv
.env\Scripts\activate   # Windows
source venv/bin/activate  # Linux/Mac
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

Dependencies include: `pandas`, `numpy`, `dash`, `plotly`.

---

## Running the Project

### 1. Run ETL

```powershell
python run_etl.py
```

* Reads `data/sales.csv`
* Cleans and transforms the data
* Loads it into `db/warehouse.db`
* Output: `ETL completed successfully!`

### 2. Run the Dashboard

```powershell
python dashboards/app.py
```

* Open in browser: `http://127.0.0.1:8050/`
* Features:

  * Product selection dropdown
  * Date range filter
  * Sales bar chart with quantity totals

### 3. Automate ETL (Optional)

```powershell
python utils/scheduler.py
```

* Automatically runs ETL on a configurable interval (default: every 60 seconds)

---

## How it Helps in the Modern World (2025+) and Future Proofing to 2030+

* **Data-Driven Decisions:** Enables small businesses and analysts to understand sales trends and optimize inventory, marketing, and operations.
* **Skill Development:** Provides hands-on experience with Python-based ETL, SQL, Pandas, and interactive dashboards—skills that remain in demand through 2030.
* **Scalable Foundation:** Can evolve from SQLite to cloud warehouses like Snowflake or BigQuery, preparing you for enterprise-level analytics.
* **Automation & AI Ready:** The scheduler and ETL framework can integrate with machine learning models and AI-driven reporting, supporting predictive analytics and automated insights.
* **Lightweight & Accessible:** Runs locally on standard hardware while teaching modern data engineering and visualization practices.
* **Future Expansion:** Add more data sources, dashboards, and analytics modules to simulate real-world business intelligence projects and pipelines.

---

## Notes & Best Practices

* Keep `venv/` in `.gitignore` for GitHub deployment.
* Always `cd` into the project folder containing `run_etl.py` before running scripts.
* Update `data/sales.csv` for new ETL runs; dashboard reflects updated data automatically.
* Future enhancements: integrate PostgreSQL, Snowflake, or AI analytics tools, add multiple dashboards, and expand ETL sources.

---

### Enjoy Your DataLite Project! 🚀
