app_name='something'
from django.urls import path

from app.views import *
urlpatterns=[
    path('index/',index,name='index'),
    path('index1/',index1,name='index1'),
]