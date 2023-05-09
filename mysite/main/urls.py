from django.urls import path
from . import views

urlpatterns = [
    path('', views.reg, name='reg'),
    path('welcome/', views.welcome, name='welcome'),
    path('verify/', views.verify, name='verify'),
]