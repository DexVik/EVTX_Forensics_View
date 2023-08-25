import json
import sqlite3
import sys
import re

infile = sys.argv[1]
tablename = sys.argv[2]
def replace_sublevel_with_string(obj):
     if isinstance(obj, dict):
        new_obj = {}
        for key, value in obj.items():
            if isinstance(value, (dict, list)):
                new_obj[key] = str(replace_sublevel_with_string(value))
            else:
                new_obj[key] = value
        return new_obj
     elif isinstance(obj, list):
        new_list = []
        for item in obj:
            if isinstance(item, (dict, list)):
                new_list.append(replace_sublevel_with_string(item))
            else:
                new_list.append(item)
        return new_list
     else:
        return obj


# Parse JSON string into a Python data structure (list of dictionaries)
with open(infile, encoding='ASCII') as lumpy_json_file:
    json_file = json.load(lumpy_json_file)

json_data = []

for x in json_file:
    json_data.append(replace_sublevel_with_string(x))

# Create an SQLite database (or connect to an existing one)
db_connection = sqlite3.connect('Forensics.db')
cursor = db_connection.cursor()
keys = list(json_data[0][0].keys())
s=str(re.escape("Account Name:\t\t"))
e=str(re.escape("\r"))

for i in range(0,len(json_data[0])):
    if json_data[0][i]['Message']:
        if "Account Name" in json_data[0][i]['Message']:
            json_data[0][i]['UserId'] = res=re.findall(s+"(.*)"+e,json_data[0][i]['Message'])[0]

# Create a table
create_table_sql = f'''
    CREATE TABLE IF NOT EXISTS '''+ tablename + f''' (
        {", ".join(f"{column} TEXT" for column in keys)}
    )
'''
# Insert data into the table
cursor.execute(create_table_sql)
for entry in json_data[0]:
    insert_sql = f'''
        INSERT INTO '''+tablename+f''' ({", ".join(keys)})
        VALUES ({", ".join(["?"] * len(keys))})
    '''
    cursor.execute(insert_sql, [entry[column] for column in keys])

cursor.execute("SELECT count(*) FROM "+tablename+";")
x = cursor.fetchall()
# Commit changes and close the connection
db_connection.commit()
db_connection.close()
print("JSON data successfully inserted" + str(x[0]) + " Rows into the SQLite database.")