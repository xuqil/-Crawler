from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer
Engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test', encoding='utf8')
Base = declarative_base()


# 创建DBSession类型
DBSession = sessionmaker(bind=Engine)
# 创建session对象
session = DBSession()


class Interval(Base):
    __tablename__ = 'interval'

    id = Column(Integer, autoincrement=True, primary_key=True)
    start = Column(Integer)
    end = Column(Integer)


def init_db():
    Base.metadata.create_all(Engine)

# 创建表
# init_db()

# 新增数据
# session.add(Interval(start=0, end=100))
# session.commit()


# 实例行为
ins = session.query(Interval).first()
print(ins.end - ins.start)


# 类行为
ins = session.query(Interval).filter(Interval.end - Interval.start > 10).first()
print(ins.id)
