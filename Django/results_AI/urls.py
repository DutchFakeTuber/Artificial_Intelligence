from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='results_AI_index'),
    path('all-questions', views.allQuestions, name='results_AI_allQuestions'),
    path('per-question', views.perQuestion, name='results_AI_perQuestion'),
    path('how-does-it-work', views.howDoesItWork, name='results_AI_howDoesItWork')
]