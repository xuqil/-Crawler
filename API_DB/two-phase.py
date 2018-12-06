from sqlalchemy import create_engine, Column
from sqlalchemy.orm import sessionmaker
from API_DB.foreignkey import User, BlogAndTag, Tag
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import String, Integer, CHAR, BIGINT, Text
Engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test', encoding='utf8')
Engine2 = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test2', encoding='utf8')

# # 创建DBSession类型
# DBSession = sessionmaker(bind=Engine)
# # 创建session对象
# session = DBSession()

Base = declarative_base()


class Blog(Base):
    __tablename__ = 'blog3'

    id = Column(Integer, primary_key=True)
    title = Column(String(64), nullable=False)
    text = Column(Text, nullable=False)
    create = Column(BIGINT, index=True, nullable=False)


def init_db():
    Base.metadata.create_all(Engine2)

# init_db()


DBSession = sessionmaker(twophase=True)
DBSession.configure(binds={User: Engine, Blog: Engine2})
session = DBSession()

# user = User(name=u'你的名字')
# session.add(user)
# session.commit()


blog = Blog(title='哈哈', text='你好呀', create=3)
session.add(blog)
session.commit()


