from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column
from sqlalchemy.types import String, Integer
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test', encoding='utf8')
DBSession = sessionmaker(engine)

Base = declarative_base()
metadata = Base.metadata
session = DBSession()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), index=True)


class Session(Base):
    __tablename__ = 'session'

    id = Column(Integer, primary_key=True)
    user = Column(String(100), index=True)
    ip = Column(String(100))


# Base.metadata.create_all(engine)

query = session.query(Session, User.username).join(User, User.id == Session.ip)
for i in query:
    print(i)

