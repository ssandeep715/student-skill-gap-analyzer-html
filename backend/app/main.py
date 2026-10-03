from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base,engine
from .routers import students,assessment,analysis

Base.metadata.create_all(bind=engine)
app=FastAPI(title="SkillGap AI API",version="1.0.0")

app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

app.include_router(students.router,prefix="/api")
app.include_router(assessment.router,prefix="/api")
app.include_router(analysis.router,prefix="/api")

@app.get("/")
def root(): return {"message":"SkillGap AI API is running"}

@app.get("/api/health")
def health(): return {"status":"healthy"}

@app.get("/api/skills")
def skills():
    return ["Programming","Web Development","Backend Development","Database Management","Cloud Computing","DevOps","Networking","Cybersecurity","Data Analysis","Problem Solving"]

@app.get("/api/roles")
def roles():
    return ["DevOps Engineer","Cloud Engineer","Backend Developer","Full Stack Developer","Data Analyst","Cybersecurity Analyst"]
