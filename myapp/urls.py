from django.urls import path,include
from . import views
app_name = 'myapp'
urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('login/',views.Login.as_view(),name='login'),
    path('upload/',views.ProcessImage.as_view(),name='upload'),
]
