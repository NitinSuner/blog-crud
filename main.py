from fastapi import FastAPI , HTTPException , Depends
from sqlmodel import SQLModel,select,Session
from sqlalchemy.exc import OperationalError
from database import engine,get_session
from models import Blog

app = FastAPI()


@app.on_event("startup")
def  on_startup():
    try:
        SQLModel.metadata.create_all(engine)
        print("Database Sucessfully!")
    except OperationalError as e:
        print("Database connection failed:", e)

#SERVER HEALTH CHECK
@app.get("/")
def home():
    return {"massage" : "Welcome to BLOG API 1.0"}


#CREATE BLOG 
@app.post("/add_blog")
def add_blogs(blog: Blog, session: Session = Depends(get_session) ):
    session.add(blog)
    session.commit()
    session.refresh(blog)
    return blog
    # return {"massage ": f"Blog created! {blog}"}


#GET ALL BLOG DATA
@app.get("/blogs")
def get_all(session:Session=Depends(get_session)):
    return session.exec(select(Blog)).all()