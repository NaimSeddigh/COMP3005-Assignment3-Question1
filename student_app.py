import psycopg2

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host = "localhost",
            port = "5432",
            database = "student_management", #database name
            user = "postgres", #user
            password = "postgres" #password
        )
        return conn
    
    except Exception as e:
        print(f"Error connecting to database {e}")
        return None


#1. Function to get all students (as required by the assignment outline) 
def getAllStudents():
    conn = get_db_connection()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT * from students ORDER BY student_id;")
        students = cur.fetchall() # fetch all the rows from the table (as a list of queries)
        
        #print in an organized table
        print("\n---ALL STUDENTS ---")
        print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Email':<25} {'Enrollment Date'}")
        print("-" * 80)
        for student in students:
            print(f"{student[0]:<5} {student[1]:<15} {student[2]:<15} {student[3]:<25} {student[4]}")
        print()
        
    except Exception as e:
        print(f"Error retrieving students: {e}")
    finally:
        cur.close()
        conn.close()
        

#2. Function to add a new student
def addStudent(first_name, last_name, email, enrollment_date):
    conn = get_db_connection()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        cur.execute( #insert the parameter values into the table
            "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",
            (first_name, last_name, email, enrollment_date)
        )
        conn.commit()
        print(f"Student {first_name} {last_name} added successfully!")
        
    except psycopg2.IntegrityError:
        print(f"Error: Email '{email}' already exists. Please use a different email.")
    except Exception as e:
        print(f"Error adding student: {e}")
    finally:
        cur.close()
        conn.close()


#3. Function to update student email
def updateStudentEmail(student_id, new_email):
    conn = get_db_connection()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        cur.execute( #update the student email with the parameter
            "UPDATE students SET email = %s WHERE student_id = %s;",
            (new_email, student_id)
        )
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"Email for student ID {student_id} updated to {new_email}!")
        else:
            print(f"No student found with ID {student_id}.")
            
    except psycopg2.IntegrityError:
        print(f"Error: Email '{new_email}' already exists. Please use a different email.")
    except Exception as e:
        print(f"Error updating email: {e}")
    finally:
        cur.close()
        conn.close()
        

#4. Function to delete a student
def deleteStudent(student_id):
    conn = get_db_connection()
    if conn is None:
        return
    
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,)) #delete the student with the given ID
        conn.commit()
        
        if cur.rowcount > 0:
            print(f"Student with ID {student_id} deleted successfully!")
        else:
            print(f"No student found with ID {student_id}.")
            
    
    except Exception as e:
        print(f"Error deleting student: {e}")
    finally:
        cur.close()
        conn.close()
        
        
# Main menu function
def main():
    while True:
        print("\n=== Student Management System ===")
        print("1. View all students")
        print("2. Add new student")
        print("3. Update student email")
        print("4. Delete student")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            getAllStudents()
            
        elif choice == '2':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            email = input("Enter email: ")
            enrollment_date = input("Enter enrollment date (YYYY-MM-DD): ")
            addStudent(first_name, last_name, email, enrollment_date)
            
        elif choice == '3':
            try:
                student_id = int(input("Enter student ID to update: "))
                new_email = input("Enter new email: ")
                updateStudentEmail(student_id, new_email)
            except ValueError:
                print("Please enter a valid student ID (number).")
                
        elif choice == '4':
            try:
                student_id = int(input("Enter student ID to delete: "))
                deleteStudent(student_id)
            except ValueError:
                print("Please enter a valid student ID (number).")
                
        elif choice == '5':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()