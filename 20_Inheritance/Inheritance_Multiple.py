"""
Multiple Inheritance  
One child → inherits from two or more parents  
Example: Mother → Son ← Father  
Child gets features of both parents
"""

# First parent class
class Mother:
    # Method of Mother class
    def cooking(self):
        print("Mother cooks all days..")

# Second parent class
class Father:
    # Method of Father class
    def driving(self):
        print("Father drives car..")

# Child class inheriting from BOTH Mother and Father
class Son(Mother, Father):
    # Child's own method
    def study(self):
        print("Child studies")

# Creating object of Child class
s = Son()

# Calling Mother's method using Son object
s.cooking()

# Calling Father's method using Son object
s.driving()

# Calling Son's own method
s.study()
