from django.urls import path
from API_App.views import *

urlpatterns = [
    path("getStudents", view, name="view"),
    path('addStudents', add, name='add'),
    path('updateStudent/<int:id>', update, name='update'),
    path('pupdateStudent/<int:id>', pupdate, name='pupdate'),
    path('deleteStudent/<int:id>', delete, name='delete'),
]
