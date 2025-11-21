# """
# A class method is a method that belongs to the class rather than an instance.
# It can access class attributes but cannot access instance attributes directly, because it doesn’t operate 
# on a particular object.

# Decorator: @classmethod
# First parameter: cls (refers to the class itself, not the object)

# Syntax:
# class ClassName:
#     @classmethod
#     def method_name(cls, other_parameters):
#         # code

# cls is a reference to the class, not an object.
# Can modify class attributes or create alternative constructors.
# """

# # Task 10: Create a class School with:
# # class attribute: school_name
# # classmethod: change_school() to update school name
# # instance attributes: student name, grade
# # Create objects → change school name using classmethod → print changes.


# class School:
#     school_name = 'SBV'     # class attribute

#     def __init__(self, stu_name, stu_grade):        # instance attribute
#         self.stu_name = stu_name
#         self.stu_grade = stu_grade

#     @classmethod               # @classmethod is used to update or access class-level attributes.
#     def change_school(cls, new_name):
#         cls.school_name = new_name
#         print(f"My School name is {cls.school_name}.")

#     def stu_details(self):
#         print(f"My name is {self.stu_name}. \nMy grade is {self.stu_grade}")

    
# s1 = School('Drashtu', 'C')

# School.change_school('SV')
# s1.stu_details()
# print("----------")

# s2 = School('sejal', 'A')
# School.change_school()
# s2.stu_details()
# print("----------")


class Class_name:
    name = 'Drashti'

    @classmethod
    def Class_varibale_changed(cls,new_name):
        Class_name.name = new_name
        print(f"My name is {Class_name.name}.")

c1 = Class_name()

c1.Class_varibale_changed('Sejal')