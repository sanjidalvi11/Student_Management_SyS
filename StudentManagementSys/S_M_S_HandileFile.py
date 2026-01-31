from student import student_class
from fileHandLing import saveAndLode,searchStudent,RemoveStudent
from fileHandLing import DuplicateRollNumbersFind,displaystudent
from utlisfile import print_table,print_tablesingle
# File_pat='./fileHandLing/studentFile.json'
class S_M_S:
    def __init__(self):
        pass  # Initialize class

    def addStudent(self,name:str,roll:int,email:str,deparment:str):
        student_obj=student_class( name=name,
                                  roll=roll,
                                  email=email,
                                  deparment=deparment
                                  )
        student_dict=student_obj.__dict__
        racodFind=DuplicateRollNumbersFind(roll=roll)
        if racodFind:# Duplicate check
            print("-"*30)
            print(f"--- Roll number already exists for another student ---")  
            print("-"*30)
        else:
         saveAndLode(racode=student_dict)  # Save student
         print("-"*30)
         student_obj.displayStudent()  # Display added student
         print("-"*30)
         print(" --- Student record added successfully! ---")
         print("-"*30)
    
    def displayAllStudent(self):
         racod=displaystudent()  # Load all students
         if not racod:
             print("="*40)
             print("--- No student records found ---")  # Empty file
             print("="*40)
         else:
             print_table(students=racod,title="--- All Student Racod ---")
            
    def SearchStudent(self,roll:int):
        student=searchStudent(roll=roll)  # Search student
        if not student:
            print("="*50)
            print("--- Student Record Not Found ---")  # Not found
            print("="*50)
        else:
            print_tablesingle(student=student,title=f"Student Racod Roll ( {roll} ) ")
            
    def Remove_student(self,roll:int):
        
              print("="*70)
              yesorno=input(f"Are you sure you want to delete student with roll numbe {roll} ? (Y/N): ")
              print("="*70)
              if yesorno.lower()=="y":
                 student=RemoveStudent(roll=roll)  # Delete student
                 student_w=len(student)
                 print("="*student_w)
                 print(student)  # Show result
                 print("="*student_w)
              else:
                 print("="*35)
                 print("--- Thank You Cancel deletion ---")  # Cancel deletion
                 print("="*35)

