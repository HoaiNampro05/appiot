from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Home.as_view(),name='home'),
    path('login/',views.Login.as_view(),name='login'),
]
