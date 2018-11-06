from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, and_, or_, text, column, func
from sqlalchemy.orm import sessionmaker
from API_DB import test2

Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/sqla_test', encoding='utf8')

# 创建DBSession类型
DBSession = sessionmaker(bind=engine)
# 创建session对象
session = DBSession()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=20))
    fullname = Column(String(length=30))
    password = Column(String(length=40))

    def __repr__(self):
       return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullname, self.password)

def check():
    che = session.query(User)
    print(che)
    print(che.filter_by(username="asd"))

def creat_table():
    Base.metadata.create_all(engine)




if __name__ == '__main__':
    # add()
    # check()
    # creat_table()
    # print(User.__table__)
    # ed_user = User(name='ed', fullname='Ed Jones11', password='edspassword')
    # session.add(ed_user)
    # print(ed_user)
    # session.rollback()
    # session.commit()
    # for instance in session.query(User).order_by(User.id):
    #     print(instance)
    #     print(instance.name)
    # for row in session.query(User.name.label('name_label')).all():
    #     print(row.name_label)
    # for name in session.query(User).filter(User.fullname=='ED Jones').filter(User.name=='ed'):
    #     print(name.fullname)
    # for i in session.query(User).filter(User.name != 'ed'):
    #     print(i)
    # for i in session.query(User).filter(User.name.like('%ed%')):
    #     print(i)
    # for i in session.query(User).filter(User.name.in_(session.query(User.name).filter(User.name.like('%ed%')))):
    #     print(i)
    # for i in session.query(User).filter(~User.name.in_(session.query(User.name).filter(User.name.like('%ed%')))):
    #     print(i)
    # for i in session.query(User).filter(User.name != None):
    #     print(i)
    # for i in session.query(User).filter(User.name.is_(None)):
    #     print(i)
    # for i in session.query(User).filter(User.name.isnot(None)):
    #     print(i)
    # for i in session.query(User).filter(and_(User.name == 'ed', User.fullname == 'Ed Jones')):
    #     print(i)
    # for i in session.query(User.name).first():
    #     print(i)
    # for i in session.query(User).filter(text("id<:value")).params(value=4):
    #     print(i)
    # for i in session.query(User).from_statement(
    #         text("SELECT * FROM users where `name`=:name")).\
    #         params(name='ed').all():
    #     print(i)
    # stmt = "SELECT * FROM users WHERE name='ed'"
    # for i in session.execute(stmt):
    #     print(i[0])
    # for i in session.query(func.count(User.name), User.name).group_by(User.name).all():
    #     print(i)
    # for i in session.query(func.count('*')).select_from(User):
    #     print(i[0])
    for i in session.query(func.count(User.id)):
        print(i[0])