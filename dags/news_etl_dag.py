from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
import sys

sys.path.insert(0, '/mnt/c/Users/FATTANI COMPUTERS/Desktop/ETL PROJECTS/ETLPROJECT_2')

from extract import extract_news
from transform import transform_news
from load import load_news


def run_extract(**context):
    print("Starting extraction...")
    raw_data = extract_news("us")
    context['ti'].xcom_push(key='raw_data', value=raw_data)
    print("Extraction done!")

def run_transform(**context):
    print("Starting transformation...")
    raw_data = context['ti'].xcom_pull(
        key='raw_data',
        task_ids='extract_task'
    )
    transformed_data = transform_news(raw_data)
    context['ti'].xcom_push(key='transformed_data', value=transformed_data)
    print("Transformation done!")

def run_load(**context):
    print("Starting load...")
    transformed_data = context['ti'].xcom_pull(
        key='transformed_data',
        task_ids='transform_task'
    )
    load_news(transformed_data)
    print("Load done!")


with DAG(
    dag_id="news_etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@hourly",
    catchup=False,
    tags=["etl", "news"]
) as dag:

    extract_task = PythonOperator(
        task_id="extract_task",
        python_callable=run_extract
    )

    transform_task = PythonOperator(
        task_id="transform_task",
        python_callable=run_transform
    )

    load_task = PythonOperator(
        task_id="load_task",
        python_callable=run_load
    )

    extract_task >> transform_task >> load_task