from datetime import datetime

def transform_news(raw_data):
    print(f"Transforming News")
    transformed=[]
    for article in raw_data["articles"]:
        source_id = article["source"]["id"] if article["source"]["id"] else "unknown"
        source_name = article["source"]["name"]
        author = article["author"] if article["author"] else "unknown"
        title =article["title"]
        description =article["description"] if article["description"] else "No description"
        published_at = datetime.strptime(article["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")

        transformed.append({
            "source_id":source_id,
            "source_name":source_name,
            "author":author,
            "title":title,
            "description":description,
            "published_at":published_at

        })
    return transformed


