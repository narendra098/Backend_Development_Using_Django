from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('signup/',views.register,name='accounts'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]