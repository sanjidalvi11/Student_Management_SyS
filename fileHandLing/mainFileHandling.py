from utlisfile import lodeStudentFileTojsonFile, saveStudentToJsonFile, json
File_path='./fileHandLing/studentFile.json'   

def saveAndLode(racode):
     racod = lodeStudentFileTojsonFile(File_pat=File_path)  # Load existing students
     racod.append(racode)  # Add new student
     saveStudentToJsonFile(racode=racod, File_pat=File_path)  # Save updated list
     
def DuplicateRollNumbersFind(roll:int):
     racod = lodeStudentFileTojsonFile(File_pat=File_path)  # Load students
     for students in racod:
          if students["roll"] == roll:
                return True  # Duplicate found
          else:
                return False  # Not duplicate

def displaystudent():
     racod = lodeStudentFileTojsonFile(File_pat=File_path)  # Load all students
     return racod

def searchStudent(roll:int):
     racod = lodeStudentFileTojsonFile(File_pat=File_path)  # Load students
     if not racod:
           return "--- Empty file. Please add student first ---"  # Empty file
     for student in racod:
          if student["roll"] == roll:
               return student  # Found student
     return False  # Not found
               
def RemoveStudent(roll:int):
     racod = lodeStudentFileTojsonFile(File_pat=File_path)  # Load students
     if not racod:
           return "--- Empty file. Please add student first ---"  # Empty file
     newStudent = []  # List for keeping other students
     found = False  # Flag for found student
     for student in racod:
          if student['roll'] == roll:
               found = True  # Student to remove
               continue
          else:
               newStudent.append(student)  # Keep other students
               
     if found:
          saveStudentToJsonFile(File_pat=File_path, racode=newStudent)  # Save updated list
          return "--- Student record deleted successfully ---"
     else:
         
          return "--- Roll Number -- ( Not Find -- ) To Remove ---"  # Student not found

