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
#
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
# sql = '''
#         SELECT students.`name`, students.student_id, COUNT(courses.course_id), SUM(scores.number)
#         FROM scores LEFT JOIN students on scores.student_id = students.student_id
#         LEFT JOIN courses on scores.course_id = courses.course_id
#         GROUP BY students.student_id;
#         '''
#
# student = session.execute(sql)
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

s = session.query(Scores.student_id).filter(Scores.number > 60.0)
student = session.query(Students).filter(~Students.student_id.in_(s))
for i in student:
    print(str(i.student_id) + i.name)
