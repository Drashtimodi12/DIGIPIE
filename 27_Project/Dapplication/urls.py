from django.urls import path
from Dapplication.views import *

urlpatterns = [
    path('', hello, name='hi'),                  # Home route → hello view
    path('index/', indexpage, name='index'),     # /index → index page
    path('About/', about, name='about'),         # /About → about page
    path('show/<int:id>/', showStu, name='stu')  # Dynamic route with ID
]
