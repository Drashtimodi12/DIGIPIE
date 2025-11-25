from django.contrib import admin
from Dapplication.models import *

# To customize how Student table looks in admin panel
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Age', 'city')   # Show these columns
    search_fields = ('city',)                       # Search by city

# Register Student model so it appears in admin dashboard
admin.site.register(Student, StudentAdmin)
