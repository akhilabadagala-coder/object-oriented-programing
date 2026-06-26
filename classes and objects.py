class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
    def display (self):
        print("Student name",self.name)
        print("roll no",self.roll_no)
s1=Student("shiva",23)
s1.display()




