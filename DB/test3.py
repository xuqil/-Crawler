import json

data = [{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
},{
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
# with open('data.json', 'w') as file:
#     file.write(json.dumps(data))  # 将json对象转为字符串

with open('data.json', 'w') as file:
    # 保存json格式，index代表缩进
    file.write(json.dumps(data, indent=2))





