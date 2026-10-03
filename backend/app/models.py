from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,Text,func
from .database import Base

class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True)
    name=Column(String(120),nullable=False)
    email=Column(String(255),unique=True,nullable=False)
    education=Column(String(120))
    graduation_year=Column(Integer)
    experience_level=Column(String(50))
    target_role=Column(String(120))
    created_at=Column(DateTime(timezone=True),server_default=func.now())

class Assessment(Base):
    __tablename__="assessments"
    id=Column(Integer,primary_key=True)
    student_id=Column(Integer,ForeignKey("students.id"),nullable=False)
    competencies=Column(Text,nullable=False)
    created_at=Column(DateTime(timezone=True),server_default=func.now())

class Analysis(Base):
    __tablename__="analyses"
    id=Column(Integer,primary_key=True)
    student_id=Column(Integer,ForeignKey("students.id"),nullable=False)
    target_role=Column(String(120),nullable=False)
    match_percentage=Column(Integer)
    summary=Column(Text)
    created_at=Column(DateTime(timezone=True),server_default=func.now())
