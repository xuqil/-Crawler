from sqlalchemy import create_engine
from sqlalchemy import Column
from sqlalchemy.types import String, Integer, CHAR, BIGINT, Text
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
Engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test', encoding='utf8')
metadata = Base.metadata


class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    text = Column(Text, nullable=False)
    user = Column(CHAR(32), index=True, nullable=False)
    create = Column(BIGINT, index=True, nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    username = Column(String(32), index=True, nullable=False)
    password = Column(String(64), nullable=False)


def init_db():
    Base.metadata.create_all(Engine)


def drop_db():
    Base.metadata.drop_all(Engine)


if __name__ == '__main__':
    init_db()
    # drop_db()
