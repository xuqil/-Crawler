from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from API_DB.foreignkey import User, Blog, BlogAndTag, Tag
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
# user = User(name='小猪猪', username=u'笨蛋小猪', password='4554')
# session.add(user)
# session.flush()
# blog = Blog(title=u'第一篇作文', text='你是大笨蛋', user_id=user.id, create=1)
# session.add(blog)
# session.commit()

#
# """下面注意在模板定义user_obj和blog_list"""
# # 查询Blog对的user
# print(session.query(Blog).get(1).user_obj)
# print(session.query(Blog).get(1).user_obj.id)
# # 查询user的全部blog
# result = session.query(User).get(1).blog_list
# for i in result:
#     print(i.title)
#
# '''
# 这种关系的定义, 并不影响查询并获取对象的行为, 不会添加额外的 join 操作. 在对象上取一个user_obj 或者取 blog_list 都是发生了一个
# 新的查询操作.上面的关系定义, 对应的属性是实际查询出的实例列表, 当条目数多的时候, 这样可能会有问题. 比如用户名下有成千上万的文章,
# 一次全取出就太暴力了. 关系对应的属性可以定义成一个 Query :
# '''

# # 这样在获取实例时就可以自由控制了:
# # 查询user下的每篇blog
# result = session.query(User).get(1).blog_list.all()
# for i in result:
#     print(i.title)
#
# #  提取该user下title为“嗨嗨”的blog
# result = session.query(User).get(1).blog_list.filter(Blog.title == '嗨嗨').first()
# print(result.title)

# # 查询编写title = “嗨嗨”的blog的user
# # 对于一对多的关系，使用any()函数查询
# result = session.query(User).filter(User.blogs.any(Blog.title == '嗨嗨')).first()
# print(result.name)
# # 查询name="小星星"作者的blog
# # 反之，对于多对一的关系，则使用has()函数查询
# blog = session.query(Blog).filter(Blog.user_obj.has(User.name == u'小星星')).first()
# print(blog.title)

# blog = session.query(Blog).first()
# print(blog.user_obj)
# print(blog.user_obj.name)
# print(session.query(Blog))

#
# user = session.query(User).first()
# print(user.name)
#
# # user = User(name=u'小星星')
# # 小星星创建两篇blog
# # session.add_all([Blog(title=u'A', text=u'呜呜呜', create=1, user_obj=user),
# #                  Blog(title=u'B', text=u'顶顶顶顶', create=2, user_obj=user)])
# # session.commit()
# # 通过blogs = relationship('Blog')查询第一个user下的blog
# user = session.query(User).first()
# print(user.blogs)


blog = session.query(Blog).filter(Blog.title == '测试').one()  # 获取title为“测试”的blog
print(blog.tag_list)  # 该blog对应的Tag对象
print(session.query(Blog).filter(Blog.title == '测试'))  # 对应的SQL查询语言
for i in blog.tag_list:  # 遍历blog对应的Tag对象
    print(i.name)  # 每个Tag的name
