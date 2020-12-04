from django.urls import path
from mainPage import views

urlpatterns = [
    path('', views.main, name='mainPage_index')
]