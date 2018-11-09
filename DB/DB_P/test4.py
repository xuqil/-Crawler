import pymysql

db = pymysql.connect(host='localhost', user='root', password='19218', port=3306, db='spiders')
cursor = db.cursor()
data = {
    'id': '12021',
    'name': 'Bob',
    'age': 20
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
try:
    if cursor.execute(sql, tuple(data.values())):
        print('Successful')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()