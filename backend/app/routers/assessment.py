import json
from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Assessment
from ..schemas import AssessmentRequest

router=APIRouter(prefix="/assessment",tags=["Assessment"])

@router.post("")
def save_assessment(data:AssessmentRequest,db:Session=Depends(get_db)):
    a=Assessment(student_id=data.student_id,competencies=json.dumps(data.competencies))
    db.add(a);db.commit();db.refresh(a)
    return {"id":a.id,"message":"Assessment saved"}
