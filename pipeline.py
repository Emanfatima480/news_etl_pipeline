from extract import extract_news
from transform import transform_news
from load import load_news

def run_pipeline(country):
    print("="* 40)
    print("Starting News ETL pipeline...")
    print("="*40)

    raw_data = extract_news(country)
    if not raw_data:
        print("pipeline failed at Extract step.")
        return
    transform_data = transform_news(raw_data)

    load_news(transform_data)

    print("="* 40)
    print("Pipeline completed successfully!")
    print("="* 40)

if __name__ == "__main__":
    countries = ["us", "gb", "pk"]
    for country in countries:
        run_pipeline(country) 