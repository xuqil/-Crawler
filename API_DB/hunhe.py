from sqlalchemy import create_engine, Column, func, ForeignKey, select
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Integer, String
from sqlalchemy.ext.hybrid import hybrid_property, hybrid_method
Engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test', encoding='utf8')
Base = declarative_base()


# 创建DBSession类型
DBSession = sessionmaker(bind=Engine)
# 创建session对象
session = DBSession()


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('user4.id'), index=True)
    balance = Column(Integer, server_default='0')


class User(Base):
    __tablename__ = 'user4'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(32), nullable=False, server_default='')

    accounts = relationship('Account')

    @hybrid_property
    def balance(self):
        return sum(x.balance for x in self.accounts)


class Interval(Base):
    __tablename__ = 'interval'

    id = Column(Integer, autoincrement=True, primary_key=True)
    start = Column(Integer)
    end = Column(Integer)

    @hybrid_property
    def length(self):
        return abs(self.end - self.start)

    @hybrid_method
    def bigger(self, i):
        return self.length > i

    @length.setter
    def length(self, i):
        session.end = self.start + i

    @length.expression
    def length(self):
        return func.abs(self.end - self.start)


def init_db():
    Base.metadata.create_all(Engine)

# 创建表
# init_db()

# 新增数据
# session.add(Interval(start=0, end=100))
# session.commit()

#
# # 实例行为
# ins = session.query(Interval).first()
# print(ins.end - ins.start)
#
#
# # 类行为
# ins = session.query(Interval).filter(Interval.end - Interval.start > 10).first()
# print(ins.id)

#
# # ins = session.query(Interval).filter(Interval.length > 10).first()
# ins = session.query(Interval).filter(Interval.bigger(10)).first()
#
# print(ins.id)
# print(ins.bigger(1))


# ins = session.query(Interval).filter(Interval.length > 1).first()
# print(ins.id)

# 查询时
user = session.query(User).first()
print(user.balance)
