from fastapi import FastAPI,HTTPException,Depends
from pydantic import BaseModel,Field
from uuid import UUID
from typing import List
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db =SessionLocal()
        yield db
    finally :db.close()

class Book(BaseModel):
    title:str = Field(min_length=1,max_length=255)
    author:str = Field(min_length=1,max_length=100)
    discription:str = Field(min_length=1,max_length=100)
    rating:int =Field(gt=-1,lt=101)

BOOKS:List[Book]=[]
@app.get("/")
def read_api(db: Session = Depends(get_db)):
    all_data = db.query(models.Books).all()
    return {"all_books":all_data}

@app.post("/")
def create_book(book:Book,db: Session = Depends(get_db)):
    book_model = models.Books()
    book_model.title=book.title
    book_model.description=book.discription
    book_model.rating=book.rating
    book_model.author=book.author
    db.add(book_model)
    db.commit()
    print(book_model)
    return book

@app.put("/{book_id}")
def update_book(book_id:int,book:Book,db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if not book_model:
        raise HTTPException(
            status_code=401,
            detail="not found with this id"
        )
    book_model.title=book.title
    book_model.description=book.discription
    book_model.rating=book.rating
    book_model.author=book.author
    db.add(book_model)
    db.commit()
    print(book_model)
    return book

@app.delete("/delete_book{book_id}")
def delete_book(book_id:int,db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == book_id).first()
    if not book_model:
        raise HTTPException(
            status_code=401,
            detail="we could not find any with the given id"
        )
    db.query(models.Books).filter(models.Books.id == book_id).delete()
    db.commit()
    return {
        "message":"successfully deleted the item"
    }