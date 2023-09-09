from django.urls import path
from . import views

urlpatterns = [
    path('login/', views. login, name='login'),
    path('createaccount/', views.create_account, name='create_account'),
  
]