from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, func, select, not_, or_
from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
metadata = Base.metadata


class Students(Base):
    __tablename__ = 'Students'
    student_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    gender = Column(Integer, nullable=False)


class Courses(Base):
    __tablename__ = 'Courses'
    course_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    teacher_id = Column(Integer, nullable=False)


class Scores(Base):
    __tablename__ = 'Scores'
    scores_id = Column(Integer, primary_key=True)
    student_id = Column(Integer, nullable=False)
    course_id = Column(Integer, nullable=False)
    number = Column(Float, nullable=False)


class Teachers(Base):
    __tablename__ = 'Teachers'
    teacher_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


engine = create_engine('mysql+mysqlconnector://root:19218@127.0.0.1:3306/django_db1', encoding='utf8')
# Base.metadata.create_all(engine)

DBSession = sessionmaker(engine)
session = DBSession()


# student = session.query(Students, func.avg(Scores.number).label('average')).\
#     join(Scores, Students.student_id == Scores.student_id).filter(Students.student_id == Scores.student_id).all()
#
# for i, j in student:
#     print(i.name + str(j))
# print(student)
# print(type(student))
# 查询平均成绩大于60分的同学的id和平均成绩
# sql = 'SELECT students.`name` , AVG(scores.number) FROM scores ' \
#       'LEFT JOIN students on scores.student_id = students.student_id  ' \
#       'GROUP BY students.student_id HAVING AVG(scores.number) > 60;'
#
# student = session.execute(sql)
#
# for i in student:
#     print(i)
# print(student)
#
# student = session.query(Students.student_id, func.avg(Scores.number).label('avg')).\
#     join(Scores, Students.student_id == Scores.student_id).\
#     group_by(Students.student_id).having(func.avg(Scores.number) > 60)
# for i in student:
#     print(i)


# # 查询所有同学的id、姓名、选课的数、总成绩
# sql = '''
#         SELECT students.`name`, students.student_id, COUNT(courses.course_id), SUM(scores.number)
#         FROM scores LEFT JOIN students on scores.student_id = students.student_id
#         LEFT JOIN courses on scores.course_id = courses.course_id
#         GROUP BY students.student_id;
#         '''
# student = session.execute(sql)
# for i in student:
#     print(i)
#
# student = session.query(Students.student_id, Students.name,
#                         func.count(Courses.course_id).label('num'),
#                         func.sum(Scores.number).label('sum'))\
#     .join(Scores, Students.student_id == Scores.student_id)\
#     .join(Courses, Scores.course_id == Courses.course_id).group_by(Students.student_id)
# for i in student:
#     print(i)


# teacher = session.query(Teachers).filter(Teachers.name.like('李%')).count()
# print(teacher)
#
# # 查询选了黄老师课程的学生
# student = session.query(Scores.student_id).join(Courses, Scores.course_id == Courses.course_id)\
#     .join(Teachers, Courses.teacher_id == Teachers.teacher_id).filter(Teachers.name == '黄老师')
# print(student)
# for i in student:
#     print(i[0])
#
# student = session.query(Students).filter(~Students.student_id.in_(student))
# for i in student:
#     print(i.name + str(i.student_id))
# print(student)

# student = session.query(Students).filter(Scores.student_id == Students.student_id)\
#     .filter(Courses.teacher_id == Teachers.teacher_id).filter(not_(Courses.teacher_id == 2))
# for i in student:
#     print(i.name)
# print(student)

# sql = '''
#     SELECT `students`.student_id, `students`.`name` FROM `students`
#     WHERE NOT (`students`.student_id IN (SELECT `scores`.`student_id` FROM  scores
#     INNER JOIN `courses`  ON (`scores`.`course_id` = `courses`.`course_id`)
#     INNER JOIN `teachers` ON (courses.`teacher_id` = teachers.teacher_id) WHERE teachers.`name` = '黄老师'))
#     '''
#
# student = session.execute(sql)
# for i in student:
#     print(i)

# # 查询学过课程id为1和2的所有同学的id、姓名（不是并）
# students = session.query(Students).filter(Scores.student_id == Students.student_id)\
#     .filter(or_(Scores.course_id == 1, Scores.course_id == 2))
# print(students)
# for i in students:
#     print(str(i.student_id) + i.name)

# # 查询选了黄老师课程的学生
# student = session.query(Scores.student_id).join(Courses, Scores.course_id == Courses.course_id)\
#     .join(Teachers, Courses.teacher_id == Teachers.teacher_id).filter(Teachers.name == '黄老师')
# student = session.query(Students).filter(Students.student_id.in_(student))
# for i in student:
#     print(str(i.student_id) + i.name)

# # 查询所有课程成绩小于60分的同学的id和姓名
# sql = '''
#     SELECT students.student_id, students.`name` FROM students
#     WHERE NOT (students.student_id in (SELECT scores.student_id FROM scores WHERE scores.number > 60.0))
# '''
# student = session.execute(sql)
# for i in student:
#     print(str(i[0]) + i[1])

# s = session.query(Scores.student_id).filter(Scores.number > 60.0)
# student = session.query(Students).filter(~Students.student_id.in_(s))
# for i in student:
#     print(str(i.student_id) + i.name)

# 查询没有学全所有课的同学的id、姓名
# sql = '''
#     SELECT students.student_id, students.name FROM students
#     LEFT JOIN scores ON (
#     students.student_id = scores.student_id)
#     GROUP BY students.student_id HAVING COUNT(scores.course_id) < 9 ;
# '''
# student = session.execute(sql)
# for i in student:
#     print(str(i.student_id) + i.name)
#
# num = session.query(Courses).count()
# print(num)
# student = session.query(Students).join(Scores, Students.student_id == Scores.student_id)\
#     .group_by(Students.student_id).having(func.count(Scores.course_id) < num).all()
# for i in student:
#     print(str(i.student_id) + i.name)

# 查询所有学生的姓名、平均分，并且按照平均分从高到低排序
# sql = '''
#     SELECT DISTINCT students.`name`, AVG(scores.number) as avg FROM students
#     LEFT OUTER JOIN scores on (students.student_id = scores.student_id)
#     GROUP BY students.student_id ORDER BY avg DESC;
#     '''
# student = session.execute(sql)
# for i in student:
#     print(i)

# student = session.query(Students.name, func.avg(Scores.number).label('avg')).\
#     join(Scores, Students.student_id == Scores.student_id)\
#     .group_by(Students.student_id).order_by('avg desc').all()
# for i in student:
#     print(i)


# # 查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分
# student = session.query(Courses.course_id,
#                         Courses.name, func.max(Scores.number).label('max'),
#                         func.min(Scores.number).label('min'))\
#     .join(Scores, Courses.course_id == Scores.course_id)\
#     .group_by(Courses.course_id)
# for i in student:
#     print(i)
#
# sql = '''
#     SELECT DISTINCT courses.course_id, courses.`name`, MAX(scores.number), MIN(scores.number)
#     FROM courses
#     LEFT JOIN scores on (courses.course_id = scores.course_id) GROUP BY courses.course_id
# '''
# s = session.execute(sql)
# for i in s:
#     print(i)


# #  查询每门课程的平均成绩，按照平均成绩进行排序
# student = session.query(Courses.name, func.avg(Scores.number).label('avg'))\
#     .join(Scores, Courses.course_id == Scores.course_id)\
#     .group_by(Courses.course_id).order_by('avg')
# for i in student:
#     print(i)
#
# sql = '''
#     SELECT courses.`name`, AVG(scores.number) AS avg
#     FROM courses
#     LEFT JOIN scores ON (courses.course_id = scores.course_id)
#     GROUP BY courses.course_id ORDER BY avg
# '''
# s = session.execute(sql)
# for i in s:
#     print(i)


# # 统计总共有多少女生，多少男生
# man = session.query(Students).filter(Students.gender == 1).count()
# print(man)
# woman = session.query(Students).filter(Students.gender == 2).count()
# print(woman)

#
# # 将“黄老师”的每一门课程都在原来的基础之上加5分
# teacher = session.query(Scores)\
#     .join(Courses, Scores.course_id == Courses.course_id)\
#     .join(Teachers, Courses.teacher_id == Teachers.teacher_id).filter(Teachers.name == '黄老师')
# for i in teacher:
#     i.number += 5
#     print(i.number)
#     session.query(Scores).filter(Scores.scores_id == i.scores_id).update({'number': i.number})
# session.commit()


# 查询两门以上不及格的同学的id、姓名、以及不及格课程数
num = session.query(Students.student_id, Students.name,
                    func.count(Scores.course_id).label('num'))\
    .join(Scores, Students.student_id == Scores.student_id).filter(Scores.number < 60)\
    .group_by(Students.student_id).having(func.count(Scores.number < 60) >= 2)
print(num)
for i in num:
    print(i)

sql = '''
    SELECT students.student_id, students.`name`, COUNT(CASE WHEN scores.number < 60.0 THEN scores.number ELSE NULL END) AS bad_count
    FROM students
    LEFT OUTER JOIN scores ON (students.student_id = scores.student_id)
    GROUP BY students.student_id HAVING COUNT(CASE WHEN (scores.number < 60.0) THEN scores.number ELSE NULL END) >= 2
'''
num = session.execute(sql)
for i in num:
    print(i)