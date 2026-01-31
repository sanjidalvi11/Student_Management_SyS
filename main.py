from StudentManagementSys import S_M_S
from utlisfile import IntValuchacker,StrValuChaker
# =========================
# Initialize Student Management System
# =========================
sms = S_M_S()

# =========================
# Menu text
# =========================
menu = """
Welcome to the Student Record Management System!

=========== MENU ===========
1. Add Student
2. View Students
3. Search Student
4. Remove Student
5. Exit
============================
"""


# Main loop

while True:
    try:
        print(menu)
        choice = input("Enter your choice: ")

        match choice:
            case "1":  # Add student
                
                name=StrValuChaker(msg="Enter Student Name: ")
                roll = IntValuchacker(msg="Enter Roll Number: ")
                email = StrValuChaker(msg="Enter Email: ")
                deparment = StrValuChaker(msg="Enter Department: ")
                sms.addStudent(name=name, roll=roll, email=email, deparment=deparment)

            case "2":  # View all students
                sms.displayAllStudent()

            case "3":  # Search a student
                roll = IntValuchacker(msg="Enter Roll Number: ")
                sms.SearchStudent(roll=roll)

            case "4":  # Remove a student
                roll = IntValuchacker(msg="Enter Roll Number: ")
                sms.Remove_student(roll=roll)

            case "5":  # Exit
                print("="*68)
                print("Thank you for using the Student Record Management System. Goodbye!")
                print("="*68)
                break

            case _:  # Invalid choice
                print("Invalid choice. Please enter 1-5.")

    except Exception as e:
        print("="*80)
        print(f"Error: {e}")
        print("="*80)
