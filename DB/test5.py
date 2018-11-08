import csv

# with open('data1.csv', 'w') as csvfile:
#     writer = csv.writer(csvfile, delimiter=' ')  # 改变分隔符
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10004', 'Mile', '20'])
#     writer.writerow(['10002', 'Bob', '21'])
#     writer.writerow(['10004', 'Jordan', '21'])

with open('data2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ')  # 改变分隔符
    writer.writerow(['id', 'name', 'age'])
    writer.writerows([['10004', 'Mile', '20'], ['10002', 'Bob', '21'], ['10004', 'Jordan', '21']])


