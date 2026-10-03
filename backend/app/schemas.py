from pydantic import BaseModel,EmailStr
from typing import Optional,Dict

class StudentCreate(BaseModel):
    name:str
    email:EmailStr
    education:Optional[str]=None
    graduation_year:Optional[int]=None
    experience_level:Optional[str]=None
    target_role:Optional[str]=None

class StudentResponse(StudentCreate):
    id:int
    class Config:
        from_attributes=True

class StudentUpdate(BaseModel):
    target_role:Optional[str]=None

class AssessmentRequest(BaseModel):
    student_id:int
    competencies:Dict[str,str]
