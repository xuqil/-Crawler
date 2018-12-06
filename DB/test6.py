import csv

# # 字典的写入
# with open('data.csv', 'a') as csvfile:
#     fieldnames = ['id', 'name', 'age']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerow({'id': '1001', 'name': 'Mike', 'age': 20})
#     writer.writerow({'id': '1004', 'name': 'Dike', 'age': 20})# 字典的写入

# 写入中文
with open('data.csv', 'a', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '1001', 'name': '猪仔', 'age': 20})
    writer.writerow({'id': '1004', 'name': '小猪', 'age': 20})