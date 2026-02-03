import json
import re

#Helpar funtion
#string valu Input  funtion

#Email validetion chaker
def inputEmailChacker(msg:str):
    while True:
        Email=input("Enter Email:").strip()
        pattern = r"^\w+@(gmail|yahoo|email)\.com$"
        if re.match(pattern,Email):
            break
        else:
            print("--- Invaliad Email ---")
    return Email
def StrValuChaker(msg:str):
    
       while True:
           try:
             valu = input(msg).strip()
             if valu=="":
              print("--- Spass Input ---")
             elif valu.isdigit():
               print("--- Input valu must be Str ---")
             else:
                 break
                      
           except Exception as error:
             print(error)
       return valu          # if all condition is True Return valo to main funtion when call 
      

# just intger input work   
def IntValuchacker(msg:str):
    
      while True:
          try:
           roll = input(msg)
           pattern=r"^\d{5}$"
           if re.match(pattern,roll):
            break
           else:
            print("Enter a valid roll inside ( Must 5 number) ")
        
          except Exception as valueror:
           print(valueror)  
           
      return roll    # if all condition is True Return valu to main funtion when call 
      


def saveStudentToJsonFile(racode:dict,File_pat:str):
    with open(File_pat,"w") as fp:
        racode=json.dump(racode,fp=fp,indent=4)
        return racode

def lodeStudentFileTojsonFile(File_pat:str):
    try:
       with open(File_pat,"r") as fp:
        
         racode=json.load(fp)
         return racode
    except Exception as _:
      return []
# def ReadJsonfile(FilePath:str):
#     try:
#        with open(FilePath,"r") as fp:
        
#          racode=json.load(fp)
#          return racode
#     except Exception as _:
#       return []
      
def print_table(students, title=""):
    if not students:
       return 
    name_w = max(len(s["name"]) for s in students)
    roll_w = max(len(str(s["roll"])) for s in students)
    email_w = max(len(s["email"]) for s in students)
    dept_w = max(len(s["deparment"]) for s in students)
    # Table width
    table_w = 8 + name_w + roll_w + email_w + dept_w
    
    print("_" * table_w)
    print(title)
    print("=" * table_w)
    print(f"{'No':<3} {'Name':<{name_w}} {'Roll':<{roll_w}} {'Email':<{email_w}} {'Deparment':<{dept_w}}")
    for i, s in enumerate(students,start=1):
        print("-" * table_w)
        print(f"{i:<3} {s['name']:<{name_w}} {s['roll']:<{roll_w}} {s['email']:<{email_w}} {s['deparment']:<{dept_w}}")
        print("=" * table_w)
def print_tablesingle(student: dict, title="--- Student Record ---"):
    """
    Prints a single student record in a table format.
    Safe for use with any dict representing a student.
    """

    # Safety check
    if not isinstance(student, dict):
        print("Error: Provided student is not a dictionary!")
        return

    # Extract values and calculate widths
    name_w = len(student.get("name", ""))
    roll_w = len(str(student.get("roll", "")))
    email_w = len(student.get("email", ""))
    dept_w = len(student.get("deparment", ""))

    # Table width
    table_w = 8 + name_w + roll_w + email_w + dept_w

    # Print table
    print("_" * table_w)
    print(title)
    print("=" * table_w)
    print(f"{'Name':<{name_w}} {'Roll':<{roll_w}} {'Email':<{email_w}} {'Deparment':<{dept_w}}")
    print("-" * table_w)
    print(f"{student.get('name',''):<{name_w}} {student.get('roll',''):<{roll_w}} {student.get('email',''):<{email_w}} {student.get('deparment',''):<{dept_w}}")
    print("=" * table_w)
