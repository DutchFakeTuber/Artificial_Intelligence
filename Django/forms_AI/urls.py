import sys
sys.path.append('..')
from django.urls import path
from forms_AI import views

urlpatterns = [
    path('', views.index, name='forms_AI_index')
]