from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('addtask/', views.addtask, name='addtask'),
    path('savetask/', views.savetask, name='savetask'),
    path('deletetask/<int:id>', views.deletetask, name='deletetask'),
    path('edittask/<int:id>', views.edittask, name='edittask'),

    
]