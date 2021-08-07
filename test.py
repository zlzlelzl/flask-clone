import csv
import sqlite3
conn = sqlite3.connect("db_6.sqlite")   # 저장할 DB파일 이름
curs = conn.cursor()

curs.execute("CREATE TABLE measures (timestamp INTEGER, measure INTEGER)")
# TABLE : measures , 컬럼이름 : (timestamp , measure)

reader = csv.reader(open('data_1.csv', 'r'))   # CSV파일 읽기모드로 열기
for row in reader:  # for 반복문을 통하여 DB에 작성
    to_db = [(row[0]), (row[1])]
    curs.execute(
        "INSERT INTO measures (timestamp, measure) VALUES (?, ?);", to_db)

conn.commit()  # 커밋 (쌓아둔 명령 실행)
conn.close()
