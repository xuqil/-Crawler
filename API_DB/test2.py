# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, String, Text, text,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql.types import LONGBLOB
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata

#答案记录
class AnswerRecond(Base):
    __tablename__ = 'AnswerRecond'
#primary主键，unique唯一，nullable非空
    AnswerGUID = Column(Integer, primary_key=True)
    QuestionGUID = Column(Integer, nullable=False, server_default=text("'0'"))
    StudentID = Column(Integer, nullable=False, server_default=text("'0'"))#学生编号
    AnswerTime = Column(DateTime, nullable=False)
    AnswerItem = Column(Text)
    Correct = Column(Integer, server_default=text("'0'"))
    QuizModeType = Column(Integer, nullable=False)

#班级课程
class ClassCourse(Base):
    __tablename__ = 'ClassCourses'

    CoursesGUID = Column(Integer, primary_key=True)
    TeacherID = Column(Integer, nullable=False)#老师编号
    CourseID = Column(Integer, nullable=False)
    ClassID = Column(Integer, nullable=False)
    StartTime = Column(DateTime)
    EndTime = Column(DateTime)
    CourseEvaluate = Column(Integer)
    TeacherEvaluate = Column(Text)
    Comment = Column(Text)
    Reviewer = Column(Text)
    ItemNum = Column(Integer, nullable=False)

#课程计划
class CourseSchedule(Base):
    __tablename__ = 'CourseSchedule'

    ItemNum = Column(Integer, primary_key=True)
    CourseID = Column(Integer, nullable=False)#课程编号
    StartTime = Column(DateTime, nullable=False)
    Duration = Column(Integer, nullable=False)#学期
    CourseNum = Column(Integer, nullable=False)#课程数目

#课件管理
class CourseWare(Base):
    __tablename__ = 'CourseWare'

    WareID = Column(Integer, primary_key=True)#课件编号
    CourseID = Column(Integer, nullable=False)
    WareName = Column(String(100))#课件名称
    WarePath = Column(Text)#课件路径

#问题选项
class QuestionItem(Base):
    __tablename__ = 'QuestionItem'

    ItemGUID = Column(Integer, primary_key=True)
    ItemNo = Column(Text)
    QuestionGUID = Column(Integer, nullable=False)
    ItemValue = Column(Text, nullable=False)
    IsRight = Column(Integer)
    IsPicture = Column(Integer)
    PictureData = Column(LONGBLOB)

#问题记录
class QuestionRecond(Base):
    __tablename__ = 'QuestionRecond'

    QuestionGUID = Column(Integer, primary_key=True)
    CoursesGUID = Column(Integer, nullable=False)
    TeacherID = Column(Integer, nullable=False)
    QuestionType = Column(Integer)
    QuestionTime = Column(DateTime, nullable=False)
    QuestionValue = Column(Text)
    ItemType = Column(Integer)
    IsPicQuestion = Column(Integer)

#年级管理
class StandardClass(Base):
    __tablename__ = 'StandardClasses'

    ClassID = Column(Integer, primary_key=True)
    GradeID = Column(Integer, nullable=False)
    ClassName = Column(String(100), nullable=False)
    ClassType = Column(Integer)
    SchoolID = Column(Integer, nullable=False)
    StudentCount = Column(Integer, nullable=False)
    ClassroomID = Column(Integer, nullable=False)
    ClassTeacher = Column(Integer, nullable=False)
    DeputyClassTeacher = Column(Integer)#副班主任

#班级管理
class StandardClassroom(Base):
    __tablename__ = 'StandardClassroom'

    ClassroomID = Column(Integer, primary_key=True)
    ClassroomValue = Column(Text, nullable=False)

#标准课程
class StandardCourse(Base):
    __tablename__ = 'StandardCourse'

    CourseID = Column(Integer, primary_key=True)
    CourseName = Column(String(100), nullable=False)
    TeacherID = Column(Integer, nullable=False)
    ClassID = Column(Integer, nullable=False)
    ClassroomID = Column(Integer)
    ClassHour = Column(Integer)

#学生评价
class StuCourseEvaluate(Base):
    __tablename__ = 'StuCourseEvaluate'

    StuEvaluateGUID = Column(Integer, primary_key=True)
    CourseGUID = Column(Integer, nullable=False)
    StudentID = Column(Integer, nullable=False)
    Evaluate = Column(Text, nullable=False)
    EvaluateTime = Column(DateTime, nullable=False)

#学生信息
class StudentInfo(Base):
    __tablename__ = 'StudentInfo'

    ClassID = Column(Integer, nullable=False)
    StudentID = Column(Integer, primary_key=True)
    StudentName = Column(String(100), nullable=False)
    Sex = Column(Integer, nullable=False)
    ContactWay = Column(Text)
    IdCard = Column(String(100))
    RowCount = Column(Integer)
    ColumnCount = Column(Integer)
    EntranceTime = Column(DateTime, nullable=False)
    StudentCadre = Column(Integer)

#系统参数
class SystemParameter(Base):
    __tablename__ = 'SystemParameter'

    ParameterType = Column(String(100), primary_key=True, nullable=False)
    ParameterNO = Column(Integer, primary_key=True, nullable=False)
    Value = Column(Text, nullable=False)
    Revisable = Column(Integer, nullable=False)

#用户cookie
class UserCookie(Base):
    __tablename__ = 'UserCookie'

    UserID = Column(Integer, primary_key=True)
    CookieValue = Column(Text, nullable=False)
    DelTime = Column(DateTime, nullable=False)

#用户信息
class UserInfo(Base):
    __tablename__ = 'UserInfo'

    UserID = Column(Integer, primary_key=True)
    CellPhone = Column(String(100), nullable=False)
    Name = Column(String(100), nullable=False)
    Sex = Column(Integer, nullable=False)
    PassWord = Column(String(100), nullable=False)
    UserType = Column(Integer, nullable=False)
    IdCard = Column(String(100), nullable=False)
    PositionInfo = Column(Text, nullable=False)
    InductionTime = Column(DateTime, nullable=False)
    SchoolID = Column(Integer, nullable=False)
    ClassID = Column(Integer)
    Email = Column(String(100))
    LastLoginTime = Column(DateTime)

engine = create_engine('mysql+pymysql://root:19218@127.0.0.1:3306/test1', encoding='utf8')
Base.metadata.create_all(engine)
