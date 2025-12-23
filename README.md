Hospital Management System (Python + MySQL)
Overview

This project implements a menu-driven Hospital Management System using Python and MySQL, designed to simulate real-world interactions between hospital staff (administrators, doctors, interns) and patients.

The system supports:

Role-based access (Admin / Doctor / Patient)

Secure database access using MySQL connection pooling

CRUD operations on hospital staff records

Patient appointment booking

Emergency services (medicines and ambulance)

The application runs entirely in the command-line interface (CLI) and demonstrates practical database-backed application development in Python.

System Architecture
User (CLI)
   │
   ▼
Menu-driven Interface
   │
   ▼
Python Application Logic
   │
   ▼
MySQL Connection Pool
   │
   ▼
MySQL Database (employees, doctor, patient tables)

Technologies Used

Python 3

MySQL

mysql.connector.pooling – connection pooling

tabulate – formatted table output

CLI-based user interaction

Database Configuration

The application connects to a MySQL database using a connection pool:

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "jay",
    "database": "employees"
}


Connection pooling improves:

Performance

Resource utilization

Concurrent database access

User Roles and Features
1. Patient Module

Patients can access the system without authentication.

Available Features

Book a medical appointment

Purchase emergency medicines

Request ambulance service

Appointment Booking

Stores patient phone number, name, sex, age, and address into the patient table.

2. Admin / Staff Module

Access is protected by credentials:

Username: admin
Password: adminpass


After authentication, staff can enter different operational modules.

3. Doctor Portal

Doctors can perform full CRUD operations on employee records.

Features

View individual doctor details

Update doctor information

Delete doctor records

Display all employee records in tabular format

Database Tables Used

DOCTOR

employees

Output

Data is displayed using tabulate for better readability.

4. HR Module (Conceptual)

The HR module is structurally present and designed to manage:

Employee records

Department information

Staff administration

(Some fields in the update logic are placeholders and intended for extension.)

Key Functional Highlights

Connection Pooling

Efficient reuse of database connections

Exception Handling

Prevents application crashes

Menu Validation

Ensures valid user input

Formatted Output

Professional table views using tabulate

Modular Design

Clear separation of concerns across functions
