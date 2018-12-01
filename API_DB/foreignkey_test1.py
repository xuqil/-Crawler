from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from API_DB.foreignkey import User, Blog
from sqlalchemy.ext.declarative import declarative_base
Engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/test', encoding='utf8')
# 创建DBSession类型
DBSession = sessionmaker(bind=Engine)
# 创建session对象
session = DBSession()


'''
session.flush()是进行数据交互，但是事物没有提交，进行数据交互后user.id才有值，后面新增blog才不会报错
定义了外键, 对查询来说, 并没有影响. 外键只是单纯的一条约束而已. 当然, 可以在外键上定义一些关联的事件操作, 比如当外键条目被删除时, 
字段置成 null , 或者关联条目也被删除等.
'''
user = User(name='小猪猪', username=u'笨蛋小猪', password='4554')
session.add(user)
session.flush()
blog = Blog(title=u'第一篇作文', text='你是大笨蛋', user_id=user.id, create=1)
session.add(blog)
session.commit()


