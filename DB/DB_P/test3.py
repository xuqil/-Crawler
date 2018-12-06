import pymysql

id = '200000'
user = 'Bob'
age = 20

db = pymysql.connect(host='localhost', user='root', password='19218', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO students(id, name, age) values (%s, %s, %s)'
try:
    cursor.execute(sql, (id, user, age))
    db.commit()
except:
    db.rollback()
db.close()