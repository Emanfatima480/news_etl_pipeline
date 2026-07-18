-- counting articles by hour
with news as(
    select * from {{ref('stg_news')}}
)
select
hour,
count(*) as total_articles
from news
group by hour
order by hour