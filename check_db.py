# this file only to check the database entries

import sqlite3

conn = sqlite3.connect('predictions.db')
cursor = conn.cursor()

# Table ka sara data nikaalna
cursor.execute("SELECT * FROM history")
rows = cursor.fetchall()

print("--- Database Entries ---")
for row in rows:
    print(row)

conn.close()