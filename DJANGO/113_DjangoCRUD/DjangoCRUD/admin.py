from django.contrib import admin
from DjangoCRUD.models import *

# Register your models here.
    


class EmployeeDisplay(admin.ModelAdmin):
    list_display = ('EMP_NAME', 'EMAIL', 'PHONE_NUMBER', 'AGE')

admin.site.register(Employee, EmployeeDisplay)