# users/urls.py

from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('agreement/', views.AgreementView.as_view(), name='agreement'),
    path('csregister/', views.CsRegisterView.as_view(), name='csregister'),
]