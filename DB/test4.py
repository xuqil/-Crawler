import json

data = [{
    "name": "王伟",
    "gender": "男",
    "birthday": "1992-10-18"
},{
    "name": "大猪头",
    "gender": "女",
    "birthday": "1995-10-18"
}]

with open('data.json', 'w', encoding='utf-8') as file:
    # 当存在中文时
    file.write(json.dumps(data, indent=2, ensure_ascii=False))