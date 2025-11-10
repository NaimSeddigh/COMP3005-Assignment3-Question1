# COMP3005-Assignment3-Question1
OVERVIEW: 
A python application that interacts with a PostgreSQL database to perform CRUD (CREATE, READ, UPDATE, DELETE) operations on student records. This application was developed for COMP 3005 Assignment 3 - Question 1

INSTALLATION AND SETUP INSTRUCTIONS:  
1. Database Setup:
   Open pgAdmin 4 and connect to your PostgreSQL server. Create a new database named "student_management". Run the following SQL to create the table and insert initial data:
   
CREATE TABLE IF NOT EXISTS students (  
student_id SERIAL PRIMARY KEY,  
first_name TEXT NOT NULL,  
last_name TEXT NOT NULL,  
email TEXT NOT NULL UNIQUE,  
enrollment_date DATE  
);

INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES   
('John', 'Doe', 'john.doe@example.com', '2023-09-01'),  
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'),  
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')  
ON CONFLICT (email) DO NOTHING; 


2. PYTHON DEPENDENCIES:
   Install the required Python package:
pip install psycopg2-binary

3. CONFIGURATION:
   Update the database connection settings in student_app.py:
   def get_db_connection():  
    try:  
        conn = psycopg2.connect(  
            host = "localhost",  
            port = "5432",  
            database = "student_management",  
            user = "postgres", #Your PostgreSQL Username  
            password = "postgres" #Your PostgreSQL password  
        )  
        return conn


RUNNING THE APPLICATION:
1. Navigate to the project directory
2. Run the Python application: python student_app.py
3. Use the menu to perform operations (1: View all students; 2: Add a new student; 3: Update a student's email; 4: Delete a student; 5: Exit the application)
