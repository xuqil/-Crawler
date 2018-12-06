from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from API_DB.foreignkey import User, Blog, BlogAndTag, Tag
Engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test', encoding='utf8')
# 创建DBSession类型
DBSession = sessionmaker(bind=Engine)
# 创建session对象
session = DBSession()


# 修改用户名字，如果失败则回滚，相当于什么事都没发生
# try:
#     user = session.query(User).first()
#     user.name = u'改名字'
#     session.commit()
# except:
#     session.rollback()
#
#
# session.query(User).with_for_update().first()
# session.query(User).with_for_update(read=True).first()
#
# # 完整形式
# session.query(User).with_for_update(read=False, nowait=False, of=None)

#
# u1 = User(name=u'用户1')
# u2 = User(name=u'用户2')
#
# u3 = User(name=u'用户3')
# # session.begin_nested()
# # session.add(u3)
# # session.rollback()  # rolls back u3, keeps u1 and u2,并没有添加用户
# #
# # session.commit()
# #
#
# # 使用上下文对象可以创建用户
# records = [u1, u2, u3]
# for record in records:
#     try:
#         with session.begin_nested():
#             session.merge(record)
#     except:
#         print("%s" % record)
#
# session.commit()

user = User(name='乐乐')
session.begin_nested()  # 使用该语句时是最外层事务提交才会生效，最外层是rollback，因此不会添加用户
session.add(user)
session.commit()
session.rollback()





