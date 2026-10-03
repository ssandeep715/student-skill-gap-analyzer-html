import json
from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import Student,Assessment,Analysis

router=APIRouter(prefix="/analysis",tags=["Analysis"])

ROLE_REQUIREMENTS={
"DevOps Engineer":["Programming","Cloud Computing","DevOps","Networking","Problem Solving"],
"Cloud Engineer":["Programming","Cloud Computing","Networking","DevOps","Problem Solving"],
"Backend Developer":["Programming","Backend Development","Database Management","Problem Solving","Web Development"],
"Full Stack Developer":["Programming","Web Development","Backend Development","Database Management","Problem Solving"],
"Data Analyst":["Programming","Database Management","Data Analysis","Problem Solving","Communication"],
"Cybersecurity Analyst":["Networking","Cybersecurity","Linux","Problem Solving","Programming"]
}
COMPETENCY_KEYS={
"Programming":"programming","Web Development":"web","Backend Development":"backend",
"Database Management":"database","Cloud Computing":"cloud","DevOps":"devops",
"Networking":"network","Cybersecurity":"security","Data Analysis":"data","Problem Solving":"problem"
}

@router.get("/latest/{student_id}")
def latest(student_id:int,db:Session=Depends(get_db)):
    student=db.get(Student,student_id)
    if not student: raise HTTPException(404,"Student not found")
    assessment=db.query(Assessment).filter(Assessment.student_id==student_id).order_by(Assessment.id.desc()).first()
    if not assessment: raise HTTPException(404,"Complete assessment first")
    data=json.loads(assessment.competencies)
    required=ROLE_REQUIREMENTS.get(student.target_role,ROLE_REQUIREMENTS["DevOps Engineer"])
    level_score={"No experience":0,"Beginner":1,"Intermediate":2,"Advanced":3}
    strengths=[];gaps=[]
    for skill in required:
        key=COMPETENCY_KEYS.get(skill,skill.lower().replace(" ","_"))
        level=data.get(key,"No experience")
        if level_score.get(level,0)>=2: strengths.append(skill)
        else: gaps.append({"skill":skill,"priority":"HIGH" if level_score.get(level,0)==0 else "MEDIUM"})
    match=round(len(strengths)/len(required)*100) if required else 0
    existing=db.query(Analysis).filter(Analysis.student_id==student_id).order_by(Analysis.id.desc()).first()
    summary=f"You currently cover {len(strengths)} of {len(required)} core competencies for {student.target_role}."
    if not existing or existing.match_percentage!=match:
        a=Analysis(student_id=student_id,target_role=student.target_role or "DevOps Engineer",match_percentage=match,summary=summary)
        db.add(a);db.commit()
    return {"match_percentage":match,"strengths":strengths,"gaps":gaps,"summary":summary}
