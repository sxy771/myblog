from django.urls import path
from . import views

urlpatterns = [
    path('', views.Resume.as_view(), name='resume'),
]
