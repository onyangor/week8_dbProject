-- Create and select the database
CREATE DATABASE IF NOT EXISTS library_db;
USE library_db;

-- Drop tables if they exist
DROP TABLE IF EXISTS Borrowings, Books, Members;

-- Create Members table
CREATE TABLE Members (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Create Books table
CREATE TABLE Books (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100),
    isbn VARCHAR(20) UNIQUE
);

-- Create Borrowings table (Many-to-Many relationship)
CREATE TABLE Borrowings (
    borrowing_id INT PRIMARY KEY AUTO_INCREMENT,
    member_id INT,
    book_id INT,
    borrow_date DATE,
    return_date DATE,
    FOREIGN KEY (member_id) REFERENCES Members(member_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);

-- Sample data
INSERT INTO Members (name, email) VALUES 
('Alice Johnson', 'alice@example.com'),
('Bob Smith', 'bob@example.com');

INSERT INTO Books (title, author, isbn) VALUES
('1984', 'George Orwell', '1234567890'),
('To Kill a Mockingbird', 'Harper Lee', '0987654321');

INSERT INTO Borrowings (member_id, book_id, borrow_date) VALUES
(1, 1, '2025-05-01'),
(2, 2, '2025-05-02');
