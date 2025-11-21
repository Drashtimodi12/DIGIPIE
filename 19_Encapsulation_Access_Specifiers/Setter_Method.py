class A:

    def __init__(self, name):
        # Private attribute (cannot be accessed directly outside the class)
        self.__stu_name = name
    
    # Getter Method → Used to get/access private data
    def get_name(self):
        return self.__stu_name

    # Setter Method → Used to update/change private data
    def set_name(self, new_name):
        self.__stu_name = new_name


# Creating object with initial name 'Drashti'
a = A('Drashti')
print(a.get_name())        # Output: Drashti

# Updating private name using setter method
a.set_name('Sejal')
print(a.get_name())        # Output: Sejal
