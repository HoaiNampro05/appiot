import base64
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from retinaface import RetinaFace
import numpy as np
import cv2
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

def detect_faces(frame):
    obj = RetinaFace.detect_faces(frame)
    for key in obj.keys():
        identify = obj[key]
        facial_area = identify['facial_area']
        cv2.rectangle(frame, (facial_area[2], facial_area[3]), (facial_area[0], facial_area[1]), (0, 255, 0), 2)
    return frame

class  ProcessImage(View):
    def post(self,request):
        if request.method == 'POST':
                image_data = request.FILES['image'].read()
                nparr = np.frombuffer(image_data, np.uint8)
                img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
                processed_img =detect_faces(img)
                _, img_encoded = cv2.imencode('.jpg', processed_img)
                img_base64 = base64.b64encode(img_encoded).decode('utf-8')
                return render(request, 'myapp/processed_image.html', {'image':img_base64})
        return render(request, 'myapp/susscess_login.html')
    def get(self,request):
        pass