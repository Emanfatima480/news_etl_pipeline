-- count articles per news source

with news as (
    select * from {{ref('stg_news')}}
)
select 
source_name,
count(*) as total_articles
from news
group by source_name
order by total_articles desc