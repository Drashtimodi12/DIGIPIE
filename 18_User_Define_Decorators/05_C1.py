# Task 10: Create a class School with:
# class attribute: school_name
# classmethod: change_school() to update school name
# instance attributes: student name, grade
# Create objects → change school name using classmethod → print changes.


class School:
    school_name = 'SBV'     # class attribute

    def __init__(self, stu_name, stu_grade):        # instance attribute
        self.stu_name = stu_name
        self.stu_grade = stu_grade

    @classmethod               # @classmethod is used to update or access class-level attributes.
    def change_school(cls, new_name):
        cls.school_name = new_name
        print(f"My School name is {cls.school_name}.")

    def stu_details(self):
        print(f"My name is {self.stu_name}. \nMy grade is {self.stu_grade}")

    
s1 = School('Drashtu', 'C')

School.change_school('SV')
s1.stu_details()
print("----------")

s2 = School('sejal', 'A')
School.change_school('CK')
s2.stu_details()
print("----------")

# OP:
# My School name is SV.
# My name is Drashtu. 
# My grade is C
# ----------
# My School name is CK.
# My name is sejal.
# My grade is A
# ----------