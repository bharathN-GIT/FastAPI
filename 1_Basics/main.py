from fastapi import FastAPI , Body

app =FastAPI()

BOOKS=[{'title':'C','author':'bha','category':'programming'}
       ,{'title':'java','author':'kum','category':'web'}
       ,{'title':'python coding','author':'ask','category':'fastapi'}]

@app.get('/get_all')
def get_all():
    return BOOKS
@app.get('/get_books')
def get_home(query_param ):
    for book in BOOKS:
        if book['title'] == query_param:
            return book

@app.post('/add_book')
def add_book(new_book=Body()):
    BOOKS.append(new_book)

@app.put('/update_book')
def add_book(update_book=Body()):
    for i in range(0,len(BOOKS)):
        if BOOKS[i]["title"]==update_book["title"]:
            BOOKS[i]=update_book

@app.delete('/delete_book')
def delete_book(update_book=Body()):
    for i in range(0,len(BOOKS)):
        if BOOKS[i]["title"]==update_book["title"]:
            BOOKS.pop(i)
            break

#http:localhost:8000/docs