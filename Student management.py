
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="student_db"
    )

    cursor = con.cursor()
    print("Database connected successfully!")

except Exception as e:
    print("Error:", e)


def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    branch = input("Enter Branch: ")
    year = int(input("Enter Year: "))

    query = "INSERT INTO students (roll_no, name, branch, year) VALUES (%s, %s, %s, %s)"
    data = (roll, name, branch, year)

    cursor.execute(query, data)
    con.commit()
    print("\n✔ Student added successfully!\n")


def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    print("\n----- Student Records -----")
    for row in rows:
        print(f"Roll: {row[0]}, Name: {row[1]}, Branch: {row[2]}, Year: {row[3]}")
    print("----------------------------\n")


def search_student():
    roll = int(input("Enter Roll Number to Search: "))
    query = "SELECT * FROM students WHERE roll_no = %s"
    cursor.execute(query, (roll,))
    row = cursor.fetchone()

    if row:
        print("\nStudent Found:")
        print(f"Roll: {row[0]}, Name: {row[1]}, Branch: {row[2]}, Year: {row[3]}\n")
    else:
        print("\n❌ No student found with that roll number.\n")


def update_student():
    roll = int(input("Enter Roll Number to Update: "))

    print("\nEnter New Details")
    name = input("New Name: ")
    branch = input("New Branch: ")
    year = int(input("New Year: "))

    query = "UPDATE students SET name=%s, branch=%s, year=%s WHERE roll_no=%s"
    data = (name, branch, year, roll)

    cursor.execute(query, data)
    con.commit()

    print("\n✔ Student updated successfully!\n")


def delete_student():
    roll = int(input("Enter Roll Number to Delete: "))
    query = "DELETE FROM students WHERE roll_no=%s"

    cursor.execute(query, (roll,))
    con.commit()
    print("\n✔ Student deleted successfully!\n")


def menu():
    while True:
        print("========== Student Management System ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        print("===============================================")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            update_student()
        elif choice == 5:
            delete_student()
        elif choice == 6:
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


menu()
