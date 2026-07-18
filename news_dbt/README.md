<<<<<<< HEAD
# 📌 News ETL Pipeline

A real-world automated ETL pipeline that extracts live news headlines
from NewsAPI, transforms and cleans the data using Python, loads it
into a PostgreSQL database using a Star Schema data warehouse design,
and orchestrates it with Apache Airflow to run automatically every hour.

## 🏷️ Badges
![Python](https://img.shields.io/badge/Python-3.14-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-18-blue)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-3.2-green)

## 🚀 Features

* 🌍 Live Data — Extracts real-time news headlines from NewsAPI
* 🔄 Automated Pipeline — Apache Airflow runs the pipeline every hour automatically
* 🗄️ Star Schema Design — Professional data warehouse structure in PostgreSQL
* 🧹 Data Cleaning — Handles null values, reshapes and transforms raw API data
* 🔐 Secure Credentials — API keys and DB passwords stored safely in .env file

## 🛠️ Technologies Used

* Python
* PostgreSQL
* Apache Airflow
* psycopg2
* NewsAPI
* python-dotenv

## 📂 Project Structure
news_etl_pipeline/
│── extract.py            # Extracts data from NewsAPI
│── transform.py          # Cleans and reshapes data
│── load.py               # Loads data into PostgreSQL
│── pipeline.py           # Runs ETL manually
│── requirements.txt      # Project dependencies
│── .env                  # Credentials (not pushed to GitHub)
│── dags/
│   └── news_etl_dag.py   # Airflow DAG for automation

## 🗃️ Star Schema Design
            dim_source
                |
dim_author — fact_news — dim_time


* fact_news — main facts table (title, description)
* dim_source — news source information
* dim_author — author information
* dim_time — published time information

## ⚙️ How to Run Manually
git clone https://github.com/Emanfatima480/news_etl_pipeline.git
cd news_etl_pipeline
pip install -r requirements.txt

Create a `.env` file with your credentials:
API_KEY=your_newsapi_key
DB_HOST=localhost
DB_NAME=news_db
DB_USER=postgres
DB_PASSWORD=your_password

Then run:
python pipeline.py

## ⚡ How to Run With Airflow
airflow standalone

Open `http://localhost:8080`, enable and trigger `news_etl_pipeline` DAG.

## 📄 License & Copyright
© 2026 Eman Fatima. All Rights Reserved.
This project is for educational and portfolio purposes only.
=======
# 🥪 The Jaffle Shop 🦘

_powered by the dbt Fusion engine_

Welcome! This is a sandbox project for exploring the basic functionality of Fusion. It's based on a fictional restaurant called the Jaffle Shop that serves [jaffles](https://en.wikipedia.org/wiki/Pie_iron).

To get started:
1. Set up your database connection in `~/.dbt/profiles.yml`. If you got here by running `dbt init`, you should already be good to go.
2. Run `dbt build`. That's it!

> [!NOTE]
> If you're brand-new to dbt, we recommend starting with the [dbt Learn](https://learn.getdbt.com/) platform. It's a free, interactive way to learn dbt, and it's a great way to get started if you're new to the tool.
>>>>>>> 47162cb (News dbt project with staging mart models and sources)
