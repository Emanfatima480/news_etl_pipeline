import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

def get_connection():
    return psycopg2.connect(
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        database = os.getenv("DB_NAME"),
        password = os.getenv("DB_PASSWORD")
    )


def get_or_create_source(cursor,source_id,source_name):
    cursor.execute("select source_id from dim_source where source_id = %s", (source_id,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute("insert into dim_source (source_id,source_name) values (%s,%s) returning source_id",(source_id,source_name))
    return cursor.fetchone()[0]

def get_or_create_author(cursor,author):
    cursor.execute("select author_id from dim_author where author = %s",(author,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute("insert into dim_author (author) values (%s) returning author_id ",(author,))
    return cursor.fetchone()[0]


def get_or_create_time(cursor,published_at):
    cursor.execute("SELECT time_id FROM dim_time WHERE published_at = %s",(published_at,))
    result = cursor.fetchone()
    if result:
        return result[0]
    cursor.execute("""INSERT INTO dim_time (published_at,hour,day,month,year) VALUES (%s,%s,%s,%s,%s) RETURNING time_id
                   """,
                   (published_at,published_at.hour,published_at.day,published_at.month,published_at.year))
    return cursor.fetchone()[0]



def load_news(data):
    print(f"Loading News to star schema...")
    conn = get_connection()
    cursor = conn.cursor()

    for article in data:
        source_id = get_or_create_source(cursor,article["source_id"],article["source_name"])
        author_id=get_or_create_author(cursor,article["author"])
        time_id=get_or_create_time(cursor,article["published_at"])

        cursor.execute("""
insert into fact_news(source_id,author_id,time_id,title,description)  values (%s,%s,%s,%s,%s)""",(
    source_id,
    author_id,
    time_id,
    article["title"],
    article["description"]

))
    conn.commit()
    cursor.close()
    conn.close()
    print(f"News published successfully!")


    
    

