from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import date
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()
app = FastAPI()

# DB Connection
db = mysql.connector.connect(
    host="localhost",
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)
cursor = db.cursor(dictionary=True)

# === MODELS ===

class Member(BaseModel):
    name: str
    email: str

class Book(BaseModel):
    title: str
    author: Optional[str] = None
    isbn: Optional[str] = None

class Borrowing(BaseModel):
    member_id: int
    book_id: int
    borrow_date: date
    return_date: Optional[date] = None

# === CRUD: MEMBERS ===

@app.post("/members/")
def create_member(member: Member):
    query = "INSERT INTO Members (name, email) VALUES (%s, %s)"
    cursor.execute(query, (member.name, member.email))
    db.commit()
    return {"member_id": cursor.lastrowid, "message": "Member created"}

@app.get("/members/{member_id}")
def get_member(member_id: int):
    cursor.execute("SELECT * FROM Members WHERE member_id = %s", (member_id,))
    result = cursor.fetchone()
    if result:
        return result
    raise HTTPException(status_code=404, detail="Member not found")

@app.put("/members/{member_id}")
def update_member(member_id: int, member: Member):
    query = "UPDATE Members SET name = %s, email = %s WHERE member_id = %s"
    cursor.execute(query, (member.name, member.email, member_id))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Member not found")
    return {"message": "Member updated"}

@app.delete("/members/{member_id}")
def delete_member(member_id: int):
    cursor.execute("DELETE FROM Members WHERE member_id = %s", (member_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Member not found")
    return {"message": "Member deleted"}

# === CRUD: BOOKS ===

@app.post("/books/")
def create_book(book: Book):
    query = "INSERT INTO Books (title, author, isbn) VALUES (%s, %s, %s)"
    cursor.execute(query, (book.title, book.author, book.isbn))
    db.commit()
    return {"book_id": cursor.lastrowid, "message": "Book created"}

@app.get("/books/{book_id}")
def get_book(book_id: int):
    cursor.execute("SELECT * FROM Books WHERE book_id = %s", (book_id,))
    result = cursor.fetchone()
    if result:
        return result
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}")
def update_book(book_id: int, book: Book):
    query = "UPDATE Books SET title = %s, author = %s, isbn = %s WHERE book_id = %s"
    cursor.execute(query, (book.title, book.author, book.isbn, book_id))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book updated"}

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    cursor.execute("DELETE FROM Books WHERE book_id = %s", (book_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": "Book deleted"}

# === CRUD: BORROWINGS ===

@app.post("/borrowings/")
def create_borrowing(borrowing: Borrowing):
    query = "INSERT INTO Borrowings (member_id, book_id, borrow_date, return_date) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (borrowing.member_id, borrowing.book_id, borrowing.borrow_date, borrowing.return_date))
    db.commit()
    return {"borrowing_id": cursor.lastrowid, "message": "Borrowing record created"}

@app.get("/borrowings/{borrowing_id}")
def get_borrowing(borrowing_id: int):
    cursor.execute("SELECT * FROM Borrowings WHERE borrowing_id = %s", (borrowing_id,))
    result = cursor.fetchone()
    if result:
        return result
    raise HTTPException(status_code=404, detail="Borrowing not found")

@app.put("/borrowings/{borrowing_id}")
def update_borrowing(borrowing_id: int, borrowing: Borrowing):
    query = """
        UPDATE Borrowings 
        SET member_id = %s, book_id = %s, borrow_date = %s, return_date = %s 
        WHERE borrowing_id = %s
    """
    cursor.execute(query, (borrowing.member_id, borrowing.book_id, borrowing.borrow_date, borrowing.return_date, borrowing_id))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Borrowing not found")
    return {"message": "Borrowing updated"}

@app.delete("/borrowings/{borrowing_id}")
def delete_borrowing(borrowing_id: int):
    cursor.execute("DELETE FROM Borrowings WHERE borrowing_id = %s", (borrowing_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Borrowing not found")
    return {"message": "Borrowing deleted"}
