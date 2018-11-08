# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, Text, text,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql.types import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


#用户信息
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

#
engine = create_engine('mysql+pymysql://root:19218@127.0.0.1:3306/api_test', encoding='utf8')
Base.metadata.create_all(engine)


