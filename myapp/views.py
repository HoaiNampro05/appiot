from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.
class Home(View):
    def get(self,request):
        return render(request,'myapp/home.html')
class Login(View):
    def get(self,request):
        return render(request,'myapp/login.html')
    def post(self,request):
        user_name = request.POST.get("user_name")
        password = request.POST.get("password")
        user = authenticate(username=user_name,password=password)
        if user is None:
            return  render(request,'myapp/login.html')
        login(request,user)
        return render(request,'myapp/susscess_login.html')

