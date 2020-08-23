from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('blogMain/', views.blogMain, name='blogMain'),
]