from lib import *
from fastapi import FastAPI
import utils

app = FastAPI()

@app.get("/books/available")
def get_books_available():
    returned_books = utils.get_return_book(books, is_available=True)
    
    return {
        "status": "success",
        "message": "Get available books successfully",
        "data": returned_books
    }

@app.get("/books/borrowed")
def get_books_borrowed():
    returned_books = utils.get_return_book(books, is_available=False)
    
    return {
        "status": "success",
        "message": "Get borrowed books successfully",
        "data": returned_books
    }