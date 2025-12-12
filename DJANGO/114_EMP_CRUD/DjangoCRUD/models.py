from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Employee(models.Model):
    EMP_NAME = models.CharField(max_length=50)
    EMAIL = models.EmailField()
    PHONE_NUMBER = models.CharField(max_length=10, validators=[RegexValidator(r"^\d{10}$", message="Phone number must be 10 digits.")])
    AGE = models.IntegerField()
    EMP_PHOTO = models.ImageField(upload_to="EmpProfile")