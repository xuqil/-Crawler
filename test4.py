from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

Base = declarative_base()


class User(Base):
    # 表的名字
    __tablename__ = 'user'

    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接
engine = create_engine('mysql+pymysql://root:19218@localhost:3306/test', encoding='utf-8', echo=True)
# Base.metadata.create_all(engine)
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
# 创建session对象
session = DBSession()
# 创建新的User对象
new_user = User(id='1', name='Bob')
# 添加到session
session.add(new_user)
# 提交即保存到数据库
session.commit()
# 关闭session
session.close()

