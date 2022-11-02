import mysql.connector
from urlextract import URLExtract

# 2 much regex 4 me
extractor = URLExtract()

# MySQL Connect
db_connection = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="zadanie"
)

data = db_connection.cursor()
# Query
sql_statement = "SELECT html FROM data"
data.execute(sql_statement)

# Output
output = data.fetchall()

# Optimal would be to skip data_list, just for readability
data_list = []
for x in output:
  data_list.append(x)

url_list = []
for html in data_list:
    for u in extractor.find_urls(str(html)):
        url_list.append(u)

print(url_list)