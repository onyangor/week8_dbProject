# week8_dbProject
# 📚 Library Management API (Week 8 DB Project)

This is a simple Library Management System built using **FastAPI** and **MySQL**. It handles basic CRUD operations for Members, Books, and Borrowings. The system simulates how members borrow and return books from a library, with data stored in a relational database.

---

## 🔧 Features

-  Manage **Books**: Create, read, update, delete
-  Manage **Members**: Register, update info, remove
-  Track **Borrowings**: Record when members borrow or return books
-  Simple API interface using FastAPI
- 🗃 Backend storage using MySQL (SQL schema provided)

---

##  Setup Instructions

### Clone this repository

bash
git clone https://github.com/onyangor/week8_dbProject.git
cd week8_dbProject

Create a virtual environment and install dependencies
bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

Set up MySQL database
Start your MySQL server.

Use a MySQL client or GUI (like MySQL Workbench) to run:

sql

-- Found in library_schema.sql
-- Creates the `library_db` database and tables
Update the main.py database connection string (if needed):

python

DATABASE_URL = "mysql+mysqlconnector://root:password@localhost:3306/library_db"
Change root and password to match your MySQL credentials.

 Run the API
bash
uvicorn main:app --reload
Visit:
 Swagger docs → http://localhost:8000/docs

 Project Structure
bash

week8_dbProject/
│
├── main.py                # FastAPI app with all CRUD routes
├── requirements.txt       # Python dependencies
├── library_schema.sql     # SQL file to create and seed the database
└── README.md              # This file

![ERD](./my_ER.png)

