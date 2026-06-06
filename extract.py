import requests
import os
from dotenv import load_dotenv

load_dotenv()

def extract_news(country="Pakistan"):
    api_key = os.getenv("API_KEY")
    url=f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    print(f"Exrracting News for {country}....")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("News extracted successfully!")
        return data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None