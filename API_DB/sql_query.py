from sqlalchemy import create_engine, or_, and_
from sqlalchemy.orm import sessionmaker
from API_DB.test6 import User, Blog
from sqlalchemy.ext.declarative import declarative_base
Engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test', encoding='utf8')
# 创建DBSession类型
DBSession = sessionmaker(bind=Engine)
# 创建session对象
session = DBSession()

# result = session.query(User).filter_by(username='小明').all()
# for i in result:
#     print(i.name)
#
# result = session.query(User).filter(User.username == '小明').all()
# for i in result:
#     print(i.name)
#
# result = session.query(Blog).filter(Blog.create >= 0).all()
# for i in result:
#     print(i.create)
# result = session.query(Blog).filter(Blog.create >= 0).first()
# print(result.create)

# or查询
# result = session.query(Blog).filter(or_(Blog.create > 10, Blog.title == '小香猪'))
# for i in result:
#     print(i.title)
# and查询
result = session.query(Blog).filter(and_(Blog.create > 1, Blog.title == '小香猪')).first()
print(result.id)
result = session.query(Blog).filter(Blog.create >= 0).filter(Blog.title == '小香猪').first()
print(result.title)
result = session.query(Blog).filter(Blog.create >= 0, Blog.title == '小香猪').first()
print(result.text)
