select 
  c._id, 
  c.first_name, 
  c.last_name,
  c.d.badge_number, 
  c.updated_at 
  from {{ws}}.contacts c
  where c.updated_at > {{updated_at}}