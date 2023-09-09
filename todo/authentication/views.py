from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import User


def login(request):
    return  render(request,'/authentication/login.html')


def create_account(request):
    #return  render(request,'/authentication/createaccount.html')
# Create your views here.

    if request.method == "POST":
        name = request.POST ["name"]
        email = request.POST ["email"]
        password = request.POST ["password"]
        confirm_password = request.POST ["confirm_password"]

        user = User()
        user.name = name
        user.email = email
        user.password = password
        user.confirm_password = confirm_password

        user.save()
        return redirect('addtask')
   
    return render(request, 'createaccount.html')


