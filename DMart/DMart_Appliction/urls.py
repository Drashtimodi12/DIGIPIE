from django.urls import path, include
from .views import welcome_page

urlpatterns = [
    path('', welcome_page, name='Welcome_page')
]
