from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import Integer, Unicode
from sqlalchemy.orm import relationship, sessionmaker, joinedload

Base = declarative_base()
Engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test2', encoding='utf8')
DBSession = sessionmaker(bind=Engine)
session = DBSession()


class Node(Base):
    __tablename__ = 'node'

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(Unicode(32), nullable=False, server_default='')
    parent = Column(Integer, ForeignKey('node.id'), index=True, server_default=None)

    children = relationship('Node')
    parent_obj = relationship('Node', remote_side=[id])


def init_db():
    Base.metadata.create_all(Engine)


# init_db()

# # n = session.query(Node).filter(Node.name == u'小猪').first()
# n = session.query(Node).filter(Node.name == u'小猪').options(joinedload('parent_obj')).first()
# print(n.id)

n = session.query(Node).filter(Node.name == u'大直沽').options(joinedload('children').joinedload('children')).first()
print(n.name)
print(n.children[0].name)
print(n.children[0].children[0].name)

