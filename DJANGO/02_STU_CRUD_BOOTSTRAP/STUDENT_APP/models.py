from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Student(models.Model):
    STU_NAME = models.CharField(max_length=50)
    STU_SURENAME = models.CharField(max_length=50)
    STU_BIRTHDATE = models.DateField()
    EMAIL = models.EmailField(validators=[RegexValidator(regex=r"^[A-Za-z0-9._]+@[A-Za-z]+\.[A-Za-z]{2,}$", message="Email not valid. Write like this: guess1@gmail.com")])
    CONTACT_NUMBER = models.CharField(max_length=10, validators=[RegexValidator(regex=r"^\d{10}$", message="Contact number must be exactly 10 digits.")])
    STU_PHOTO = models.ImageField(upload_to='STUDENT_PROFILE')