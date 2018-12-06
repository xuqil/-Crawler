from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, DateTime, Integer, String, Float

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
Base.metadata.create_all(engine)
