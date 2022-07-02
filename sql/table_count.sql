select 
  '{{table}}' as table,
  count(*) as record_count
  from {{ws}}.{{table}}
  group by table