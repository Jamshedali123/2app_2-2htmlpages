app_name='nothing'
from django.urls import path
from app1.views import*

urlpatterns=[
    path('index3/',index3,name='index3'),
    path('index4/',index4,name='index4'),
]