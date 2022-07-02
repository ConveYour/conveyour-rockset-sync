import os
from dotenv import load_dotenv
from rockset import Client, Q
from pathlib import Path
import datetime

# load .env file
load_dotenv()

# get API Key
ROCKSET_API_KEY = os.getenv('ROCKSET_API_KEY')
ROCKSET_WORKSPACE = os.getenv('ROCKSET_WORKSPACE')

# instantiate client
rs = Client(api_server='api.rs2.usw2.rockset.com', api_key=ROCKSET_API_KEY)

# get rockst cursor and auto-paginate through results
def printCursor(query):
  results = rs.sql( Q(query) )
  ## set pagination to 1k
  for r in results.iter(1000):
    print(r)

# grab queries fro sql folder and hydrate with passed variables
def getQuery( file, vars = {}):
  vars['ws'] = ROCKSET_WORKSPACE
  text = Path("./sql/" + file + ".sql").read_text()
  for key in vars:
      text = text.replace('{{' + key + '}}', vars[key])
  return text

# exampmle of getting just rencently updated contacts using the updated_at timestamp
# updated_at timestamp is available on all collections (or, well, should be)
def getRecentlyUpdatedContacts():
  yesterday = datetime.date.today() - datetime.timedelta(1)
  yesterday = yesterday.strftime("%s")
  query = getQuery('recently_updated_contacts', {
    "updated_at" : yesterday
  })
  printCursor(query)
 

# get counts on all tables!
def getTableSummaries():
  tables = [ 'events', 'contacts', 'triggers', 'campaigns', 'lessons', 'lesson_items', 'lesson_progress' ]
  query = []
  for t in tables:
      tableQuery = getQuery('table_count', { 'table': t })
      query.append(tableQuery)

  query = "\nunion all\n".join(query)
  printCursor(query)


getTableSummaries()


## Get triggers
# query = getQuery('all_table_records', {
#   'table' : 'triggers t',
#   'select' : '_id, t.d.name'
# })

# query = getQuery('all_table_records', {
#   'table' : 'campaigns cmp',
#   'select' : '_id, cmp.d.name, cmp.d.internal_name'
# })

# query = getQuery('all_table_records', {
#   'table' : 'lessons l',
#   'select' : '_id, l.d.name, length(l.d.items) items_count'
# })

# query = getQuery('all_table_records', {
#   'table' : 'lesson_items li',
#   'select' : '_id, li.d.type'
# })



