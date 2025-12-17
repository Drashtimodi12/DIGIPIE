from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from STUDENT_APP.views import *

urlpatterns = [
    path('', all_students, name='all_students'),
    path('register', register_students, name='register_students'),
    path('update', update_students, name='update_students'),
    path('delete', delete_students, name='delete_students'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
