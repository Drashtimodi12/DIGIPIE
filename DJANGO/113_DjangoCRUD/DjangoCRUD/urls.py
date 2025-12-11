from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from DjangoCRUD.views import *

urlpatterns = [ 
    path('', Emp_all, name='emp_all'),
    path('emp_register/', Emp_Register, name='emp_register'),
    path('emp_update/', Emp_update, name='emp_update'),
    path('emp_delete/', Emp_delete, name='emp_delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)