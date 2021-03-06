from sqlalchemy import create_engine
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, CHAR, BIGINT, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, attributes
from sqlalchemy.orm.collections import attribute_mapped_collection, mapped_collection
from sqlalchemy.ext.associationproxy import association_proxy

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
    # user_obj = relationship('User', lazy='joined', cascade='all')

    # tag_list = relationship('Tag')  # 显示是错误的, 因为在 Tag 中并没有外键
    # tag_list = relatiaonship('BlogAndTag')
    tag_list = relationship('Tag', secondary=lambda: BlogAndTag.__table__)

    # 定义只关心的user的name
    user_name = association_proxy('user_obj', 'name')

    # 与User配合使用
    def __init__(self, title):
        self.title = title


# 要定义关系, 必有使用 ForeignKey 约束. 当然, 这里说的只是在定义模型时必有要有, 至于数据库中是否真有外键约定, 这并不重要
class User(Base):
    __tablename__ = 'users3'

    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)

    # blog_list = relationship('Blog', order_by='Blog.create', lazy="dynamic")  # 这样在获取实例时就可以自由控制了
    # collection_class=set设置查询结果为集合形式
    # blogs = relationship('Blog', collection_class=set)

    # collection_class=attributes设置查询结果为字典形式
    # blogs = relationship('Blog', collection_class=attribute_mapped_collection('title'))

    # collection_class=attributes设置查询结果为字典形式
    # blogs = relationship('Blog', collection_class=mapped_collection(lambda blog: blog.title.lower()))

    # blog_list = relationship('Blog', cascade='')
    # blog_list_auto = relationship('Blog', cascade='save-update, delete')
    # blog_list_auto = relationship('Blog', cascade='save-update, delete, delete-orphan, merge, refresh-expire')
    # blog_list_auto = relationship('Blog', cascade='delete, delete-orphan, expunge')

    # 定义只关心的blog的title
    blog_list = relationship('Blog')
    blog_title_list = association_proxy('blog_list', 'title',
                                        creator=lambda t: Blog(title=t))


class BlogAndTag(Base):
    __tablename__ = 'blog_and_tag'

    id = Column(Integer, primary_key=True)
    blog_id = Column(Integer, ForeignKey('blog3.id'), index=True)
    tag_id = Column(Integer, ForeignKey('tag.id'), index=True)
    creat = Column(BIGINT, index=True, nullable=False)


class Tag(Base):
    __tablename__ = 'tag'

    id = Column(Integer, primary_key=True)
    name = Column(String(30))

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
