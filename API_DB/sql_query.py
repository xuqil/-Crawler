from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from API_DB.test6 import User, Blog
from sqlalchemy.ext.declarative import declarative_base
Engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test', encoding='utf8')
# 创建DBSession类型
DBSession = sessionmaker(bind=Engine)
# 创建session对象
session = DBSession()

result = session.query(User).filter_by(username='小明').all()
for i in result:
    print(i.name)

result = session.query(User).filter(User.username == '小明').all()
for i in result:
    print(i.name)

