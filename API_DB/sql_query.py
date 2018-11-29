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
# result = session.query(Blog).filter(and_(Blog.create > 1, Blog.title == '小香猪')).first()
# print(result.id)
# result = session.query(Blog).filter(Blog.create >= 0).filter(Blog.title == '小香猪').first()
# print(result.title)
# result = session.query(Blog).filter(Blog.create >= 0, Blog.title == '小香猪').first()
# print(result.text)

'''
经常用到在数据库中查询中间几条数据的需求
比如下面的sql语句：
① selete * from testtable limit 2,1;
② selete * from testtable limit 2 offset 1;
注意：
1.数据库数据计算是从0开始的
2.offset X是跳过X个数据，limit Y是选取Y个数据
3.limit  X,Y  中X表示跳过X个数据，读取Y个数据
这两个都是能完成需要，但是他们之间是有区别的：
①是从数据库中第三条开始查询，取一条数据，即第三条数据读取，一二条跳过
②是从数据库中的第二条数据开始查询两条数据，即第二条和第三条。
'''
# 不懂的查询方式（是sql函数）
# offset(0)代表去第0个满足前面条件的结果（sqlservr函数）
result = session.query(Blog).filter(Blog.create > 6).offset(0).limit(1).scalar()
print(result.title)
