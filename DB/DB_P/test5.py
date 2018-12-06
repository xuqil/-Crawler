import pymysql

db = pymysql.connect(host='localhost', user='root', password='19218', port=3306, db='spiders')
cursor = db.cursor()

sql = 'UPDATE students SET age = %s where name = %s'
try:
    cursor.execute(sql, (25, 'Bob'))
    db.commit()
except:
    db.rollback()
db.close()
