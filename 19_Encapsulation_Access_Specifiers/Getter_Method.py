class A:
    # Constructor: runs automatically when object is created
    def __init__(self, name):
        # Private attribute (cannot be accessed directly outside the class)
        self.__name = name

    # Getter method: used to access the private variable safely
    def get_name(self):
        return self.__name
    
# Creating object and passing "Sejal" as name
a = A('Sejal')

# Calling getter method to print the private name
print(a.get_name())   # Output: Sejal
