from django.urls import path
from crudapp.views import *

urlpatterns = [
    path('', home, name='home'),
    path('add_data', add_data, name="add_data")
]
