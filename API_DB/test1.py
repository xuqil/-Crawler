from sqlalchemy import Column, String, create_engine, Integer, Text, DateTime, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


# class StudentInfo(Base):
#     __tablename__ = 'StudentInfo'
#
#     ClassID = Column(Integer, nullable=False)
#     StudentID = Column(Integer, primary_key=True)
#     StudentName = Column(String(100), nullable=False)
#     Sex = Column(Integer, nullable=False)
#     ContactWay = Column(Text)
#     IdCard = Column(String(100))
#     RowCount = Column(Integer)
#     ColumnCount = Column(Integer)
#     EntranceTime = Column(DateTime, nullable=False)
#     StudentCadre = Column(Integer)

# class StandardCourse(Base):
#     __tablename__ = 'StandardCourse'
#
#     CourseID = Column(Integer, primary_key=True)
#     CourseName = Column(String(100), nullable=False)
#     TeacherID = Column(Integer, nullable=False)
#     ClassID = Column(Integer, nullable=False)
#     ClassroomID = Column(Integer)
#     ClassHour = Column(Integer)


# class StandardClassroom(Base):
#     __tablename__ = 'StandardClassroom'
#
#     ClassroomID = Column(Integer, primary_key=True)
#     ClassroomValue = Column(Text, nullable=False)


# class StandardClass(Base):
#     __tablename__ = 'StandardClasses'
#
#     ClassID = Column(Integer, primary_key=True)
#     GradeID = Column(Integer, nullable=False)
#     ClassName = Column(String(100), nullable=False)
#     ClassType = Column(Integer)
#     SchoolID = Column(Integer, nullable=False)
#     StudentCount = Column(Integer, nullable=False)
#     ClassroomID = Column(Integer, nullable=False)
#     ClassTeacher = Column(Integer, nullable=False)
#     DeputyClassTeacher = Column(Integer)


# class CourseSchedule(Base):
#     __tablename__ = 'CourseSchedule'
#
#     ItemNum = Column(Integer, primary_key=True)
#     CourseID = Column(Integer, nullable=False)
#     StartTime = Column(DateTime, nullable=False)
#     Duration = Column(Integer, nullable=False)
#     CourseNum = Column(Integer, nullable=False)

# class QuestionRecond(Base):
#     __tablename__ = 'QuestionRecond'
#
#     QuestionGUID = Column(Integer, primary_key=True)
#     CoursesGUID = Column(Integer, nullable=False)
#     TeacherID = Column(Integer, nullable=False)
#     QuestionType = Column(Integer)
#     QuestionTime = Column(DateTime, nullable=False)
#     QuestionValue = Column(Text)
#     ItemType = Column(Integer)
#     IsPicQuestion = Column(Integer)
#
#
# class AnswerRecond(Base):
#     __tablename__ = 'AnswerRecond'  # 表的名字
#
#     AnswerGUID = Column(Integer, primary_key=True)
#     QuestionGUID = Column(Integer, nullable=False, server_default=text("'0'"))
#     StudentID = Column(Integer, nullable=False, server_default=text("'0'"))
#     AnswerTime = Column(DateTime, nullable=False)
#     AnswerItem = Column(Text)
#     Correct = Column(Integer, server_default=text("'0'"))
#     QuizModeType = Column(Integer, nullable=False)


class SystemParameter(Base):
    __tablename__ = 'SystemParameter'

    ParameterType = Column(String(100), primary_key=True, nullable=False)
    ParameterNO = Column(Integer, primary_key=True, nullable=False)
    Value = Column(Text, nullable=False)
    Revisable = Column(Integer, nullable=False)

# 初始化数据库连接
engine = create_engine('mysql+pymysql://root:19218@127.0.0.1:3306/edulab', encoding='utf8')
Base.metadata.create_all(engine)


