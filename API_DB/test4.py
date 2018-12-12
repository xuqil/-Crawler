from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, func, select
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

sql = '''
        SELECT students.`name`, students.student_id, COUNT(courses.course_id), SUM(scores.number) 
        FROM scores LEFT JOIN students on scores.student_id = students.student_id LEFT JOIN courses on scores.course_id = courses.course_id
        GROUP BY students.student_id;
        '''

student = session.execute(sql)
for i in student:
    print(i)

