"""
Hybrid Inheritance  
Combination of Multiple + Multilevel inheritance  

Example Structure:
    Multilevel: (A → B) → D  
    Multiple:  (B, C) → D 

Used when a program needs complex relationships
"""

# Parent Class 1 (Top-level)
class A:
    def display_a(self):
        print("class A.")

# Class B inherits from A (Multilevel: A -> B)
class B(A):
    def display_b(self):
        print("class B (inherits from A).")

# Parent Class 2 (Independent class)
class C:
    def display_c(self):
        print("class C.")

# Class D inherits from both B and C (Multiple + Multilevel = Hybrid)
class D(B, C):
    def display_d(self):
        print("class D (inherits from B and C).")


# Creating object of class D
obj = D()

# Calling method of class A (from B -> D)
obj.display_a()

# Calling method of class B (direct parent of D)
obj.display_b()

# Calling method of class C (other parent of D)
obj.display_c()

# Calling method of class D (its own)
obj.display_d()
