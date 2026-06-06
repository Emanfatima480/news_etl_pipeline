# News ETL Pipeline 📰

A real-world ETL pipeline that extracts live news headlines
from NewsAPI, transforms and cleans the data using Python,
and loads it into a PostgreSQL database using a Star Schema
data warehouse design.

## Tech Stack
- Python
- PostgreSQL
- psycopg2
- NewsAPI
- python-dotenv

## Pipeline Steps
1. Extract — pulls live news headlines from NewsAPI
2. Transform — cleans and reshapes the raw data
3. Load — saves into PostgreSQL with Star Schema

## Star Schema Design
- fact_news — main facts table (title, description)
- dim_source — news source information
- dim_author — author information
- dim_time — published time information
