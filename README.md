**Student Management System (Python + MySQL)**

A simple and beginner-friendly Student Management System built using Python and MySQL.
This is a menu-driven console project that performs complete CRUD operations:

1.Add Student

2.View Students

3.Search Student

4.Update Student

5.Delete Student


**Features**

Add new student records

View all existing student details

Update student information

Search students by roll number

Delete student records

MySQL database integration

Easy to understand and run

Beginner friendly

**Tech Stack**

Programming Language: Python
Database: MySQL
Library: mysql-connector-python

 **Database Setup**

Run this SQL script in MySQL Workbench / XAMPP / CLI:

CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    roll_no INT PRIMARY KEY,
    name VARCHAR(100),
    branch VARCHAR(50),
    year INT
);

 **How to Run the Project**
1.Install MySQL connector:
pip install mysql-connector-python

2.Update MySQL credentials in main.py (if needed):
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="student_db"
)

3️.Run the program:
python main.py

 **Sample Menu**
========== Student Management System ==========
1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit
===============================================

 **Learning Outcomes**

Through this project, you will learn:

Python + MySQL integration

CRUD database operations

Backend logic development

DB schema creation

Error handling

Menu-driven application design
