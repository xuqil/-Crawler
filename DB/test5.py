import csv

with open('data.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'name', 'age'])
    writer.writerow(['10004', 'Mile', '20'])
    writer.writerow(['10002', 'Bob', '21'])
    writer.writerow(['10004', 'Jordan', '21'])