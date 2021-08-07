import csv
import sqlite3
conn = sqlite3.connect("db_6.sqlite")   # 저장할 DB파일 이름
curs = conn.cursor()

curs.execute("SELECT 1000*timestamp, measure from measures")

results = curs.fetchall()
print(results)
