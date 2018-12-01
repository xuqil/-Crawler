from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, CHAR, BIGINT, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# from API_DB.test6 import User
Base = declarative_base()
Engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test', encoding='utf8')
metadata = Base.metadata


# class Blog(Base):
#     __tablename__ = 'blog2'
#
#     id = Column(Integer, primary_key=True)
#     title = Column(String(64), nullable=False)
#     text = Column(Text, nullable=False)
#     user_id = Column(Integer, ForeignKey(User.id), index=True, nullable=False)
#     create = Column(BIGINT, index=True, nullable=False)


class Blog(Base):
    __tablename__ = 'blog3'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    text = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users3.id'), index=True, nullable=False)
    create = Column(BIGINT, index=True, nullable=False)

    user_obj = relationship('User')


# 要定义关系, 必有使用 ForeignKey 约束. 当然, 这里说的只是在定义模型时必有要有, 至于数据库中是否真有外键约定, 这并不重要
class User(Base):
    __tablename__ = 'users3'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)

    blog_list = relationship('Blog', order_by='Blog.create', lazy="dynamic")  # 这样在获取实例时就可以自由控制了


# 关系只是 SQLAlchemy 提供的工具, 与数据库无关, 所以任何时候添加都是可以的.
# 上面的 User-Blog 是一个"一对多"关系, 通过 Blog 的 user 这个 ForeignKey , SQLAlchemy 可以自动处理关系的定义. 在查询时,
# 返回的结果自然也是, 一个是列表, 一个是单个对象:

def init_db():
    Base.metadata.create_all(Engine)


def drop_db():
    Base.metadata.drop_all(Engine)


if __name__ == '__main__':
    init_db()
    # drop_db()
