"""
Multilevel Inheritance  
Inheritance chain (Grandparent → Parent → Child)  
Example: A → B → C  
Each child inherits from the class above it
"""


# Level 1: Grandfather class (base class)
class Grandfather:
    # Method of Grandfather
    def property(self):
        print("Grandfather has land.")

# Level 2: Father inherits Grandfather
class Father(Grandfather):
    # Method of Father
    def car(self):
        print("Father has land and car.")

# Level 3: Son inherits Father
class Son(Father):
    # Method of Son
    def govement_job(self):
        print("Son has land, car, and government job.")



# Creating object of Son class (last level)
c = Son()

# Son can access Grandfather's property() because of multilevel inheritance
c.property()

# Son can access Father's car() method
c.car()

# Son's own method
c.govement_job()
