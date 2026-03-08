from fastapi import FastAPI ,Path, Query, HTTPException, Body
from pydantic import BaseModel, Field
from typing import Optional
from starlette import status


app =FastAPI()


class Book:
    id: int
    title : str
    author : str
    category : str
    def __init__(self,id,title,author,category):
        self.id=id
        self.title=title
        self.author=author
        self.category=category

class BookRequest(BaseModel):
    id : Optional[str] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    category: str = Field(min_length=1, max_length=100)

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "A new book",
                "author": "codingwithroby",
                "description": "A new description of a book",
            }
        }
    }

BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithroby', 'A very nice book!'),
    Book(2, 'Be Fast with FastAPI', 'codingwithroby', 'A great book!'),
    Book(3, 'Master Endpoints', 'codingwithroby', 'A awesome book!'),
    Book(4, 'HP1', 'Author 1', 'Book Description'),
    Book(5, 'HP2', 'Author 2', 'Book Description'),
    Book(6, 'HP3', 'Author 3', 'Book Description')
]

@app.get('/get_all')
def get_all():
    return BOOKS
@app.get('/get_books')
def get_home(query_param ):
    for book in BOOKS:
        if book['title'] == query_param:
            return book

@app.post('/add_book')
def add_book(book_request : BookRequest): #removed Body()
    new_book = Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book

@app.put("/books/update_book", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found')
    
@app.delete("/books/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            BOOKS.pop(i)
            book_changed = True
            break
    if not book_changed:
        raise HTTPException(status_code=404, detail='Item not found') #show this response

#http:localhost:8000/docs