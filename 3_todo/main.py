from fastapi import FastAPI,Depends
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session
from typing import Annotated
from models import Todos
app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def get_all(db : Annotated[Session,Depends(get_db)] ):
    return db.query(Todos).all()

# app.pst()
# func(todorequest)
# 	todo_model=TODOS(**todorequest.dict())
	
# 	db.add(new_model)
# 	db.commit()

# Put requesT:
# While updating we need to keep total naming, because, it might think we are adding new one and ID is incremented.
# Filter from db and 
# Give the value to that model by assigning request values.

# Delete request:
# filter().delete() #deletes that model.