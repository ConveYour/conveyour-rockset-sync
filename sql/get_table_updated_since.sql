SELECT 
  * 
  FROM {{ws}}.{{table}} 
  where updated_at >= UNIX_SECONDS( cast( CURRENT_DATETIME() - INTERVAL {{daysAgoStart}} DAY as timestamp ) )
  and updated_at < UNIX_SECONDS( cast( CURRENT_DATETIME() - INTERVAL {{daysAgoEnd}} DAY as timestamp ) )
  limit {{limit}}
  