import pymysql

db = pymysql.connect(host='localhost', user='root', password='19218', port=3306, db='spiders')
cursor = db.cursor()

data = {
    'id': '1202441',
    'name': 'Bob',
    'age': 21
}

table = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))

sql = 'INSERT INTO {table}({keys}) values ({values}) on duplicate key update'.format(table=table,
                                                                                     keys=keys, values=values)
update = ', '.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values())*2):
        print('OK')
        db.commit()
except:
    print('failse')
    db.rollback()
db.close()