import csv

# 字典的写入
with open('data.csv', 'a') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '1001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '1004', 'name': 'Dike', 'age': 20})