from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Student
from ..schemas import StudentCreate,StudentResponse,StudentUpdate

router=APIRouter(prefix="/students",tags=["Students"])

@router.post("",response_model=StudentResponse)
def create_student(data:StudentCreate,db:Session=Depends(get_db)):
    existing=db.query(Student).filter(Student.email==data.email).first()
    if existing: raise HTTPException(400,"Email already registered")
    s=Student(**data.model_dump())
    db.add(s);db.commit();db.refresh(s);return s

@router.get("/by-email/{email}",response_model=StudentResponse)
def get_by_email(email:str,db:Session=Depends(get_db)):
    s=db.query(Student).filter(Student.email==email).first()
    if not s: raise HTTPException(404,"Student not found")
    return s

@router.get("/{student_id}",response_model=StudentResponse)
def get_student(student_id:int,db:Session=Depends(get_db)):
    s=db.get(Student,student_id)
    if not s: raise HTTPException(404,"Student not found")
    return s

@router.put("/{student_id}",response_model=StudentResponse)
def update_student(student_id:int,data:StudentUpdate,db:Session=Depends(get_db)):
    s=db.get(Student,student_id)
    if not s: raise HTTPException(404,"Student not found")
    for k,v in data.model_dump(exclude_unset=True).items(): setattr(s,k,v)
    db.commit();db.refresh(s);return s
