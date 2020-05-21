from django.urls import path, include
from . import views
from django.contrib import admin




urlpatterns = [
    path('',views.index, name="index"),
    path('unv_yerles_giris/',views.unv_yerles_giris, name="unv_yerles_giris"),
    path('unv_yerles_giris/',views.unv_yerles_giris, name="unv_yerles_giris"),
    
]


