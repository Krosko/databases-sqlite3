import sqlite3
  
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('geek.db')
  
# cursor object
cursor_obj = connection_obj.cursor()
  
# to select all column we will use
statement = '''SELECT Name, Score FROM GEEK WHERE Score > 30'''
  
cursor_obj.execute(statement)

output = cursor_obj.fetchall()
for row in output:
  print(row)
  
connection_obj.commit()
  
# Close the connection
connection_obj.close()
