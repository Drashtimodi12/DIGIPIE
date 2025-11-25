from django.db import models

# Student model = database table
class Student(models.Model):
    Name = models.CharField(max_length=100)   # Text field for name
    Age = models.IntegerField()               # Number for age
    city = models.CharField(max_length=100)   # Text field for city

    # Shows student name in admin panel
    def __str__(self):
        return self.Name
