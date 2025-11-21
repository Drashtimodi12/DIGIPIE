class Student:
    def __init__(self, name, marks):
        self.__marks = marks    # private variable

    def get_marks(self):        # getter
        return self.__marks

    def set_marks(self, m):     # setter
        self.__marks = m
