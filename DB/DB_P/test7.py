import pymysql

db = pymysql.connect(host='localhost', user='root', password='19218', port=3306, db='spiders')
cursor = db.cursor()

sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    print('COUNT:', cursor.rowcount)
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()
except:
    print('error')
    