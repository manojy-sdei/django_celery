from django.urls import path, include
from .views import *


urlpatterns=[
    path('<task_id>',check_status,name="check_status"),
    path('', index, name="index")
]