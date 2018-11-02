from sqlalchemy import Column, DateTime, Integer, String, Text, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

Base = declarative_base()


class UserCookie(Base):
    __tablename__ = 'UserCookie'

    UserID = Column(Integer, primary_key=True)
    CookieValue = Column(Text, nullable=False)
    DelTime = Column(DateTime, nullable=False)


class UserInfo(Base):
    __tablename__ = 'UserInfo'

    UserID = Column(Integer, primary_key=True)
    CellPhone = Column(String(100), nullable=False)
    Name = Column(String(100), nullable=False)
    Sex = Column(Integer, nullable=False)
    PassWord = Column(String(100), nullable=False)
    UserType = Column(Integer, nullable=False)
    IdCard = Column(String(100), nullable=False)
    PositionInfo = Column(Text, nullable=False)
    InductionTime = Column(DateTime, nullable=False)
    SchoolID = Column(Integer, nullable=False)
    ClassID = Column(Integer)
    Email = Column(String(100))
    LastLoginTime = Column(DateTime)


# 初始化数据库连接
engine = create_engine('mysql+pymysql://root:19218@127.0.0.1:3306/edulab?charset=utf8')
Base.metadata.create_all(engine)
# Base.metadata.create_all(engine)
# 创建DBSession类型
# DBSession = sessionmaker(bind=engine)
# # 创建session对象
# session = DBSession()
# # 创建新的User对象
# new_user = User(id='1', name='Bob')
# # 添加到session
# session.add(new_user)
# # 提交即保存到数据库
# session.commit()
# # 关闭session
# session.close()

