class student_class:
    def __init__(self,name:str,roll:int,email:str,deparment:str):
        self.name=name
        self.roll=roll
        self.email=email
        self.deparment=deparment
    def displayStudent(self):
        print("="*15)
        print(f"Name: {self.name}")
        print(f"Roll: {self.roll}")
        print(f"Email: {self.email}")
        print(f"Deparment: {self.deparment}")
        print("="*15)