with source as (
    select
        f.fact_id,
        s.source_name,
        a.author,
        t.published_at,
        t.hour,
        t.day,
        t.month,
        t.year,
        f.title,
        f.description
    from {{ source('public', 'fact_news') }} f
    join {{ source('public', 'dim_source') }} s on f.source_id = s.source_id
    join {{ source('public', 'dim_author') }} a on f.author_id = a.author_id
    join {{ source('public', 'dim_time') }}   t on f.time_id   = t.time_id
)

select * from source