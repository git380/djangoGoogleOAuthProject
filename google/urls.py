from django.urls import path
from . import views

urlpatterns = [
    path('', views.toppage, name='toppage'),
    path('home/', views.home, name='home'),
]
