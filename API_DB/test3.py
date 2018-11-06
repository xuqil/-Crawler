from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from API_DB import test2

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/sqla_test', encoding='utf8')
# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
# 创建session对象
session = DBSession()

