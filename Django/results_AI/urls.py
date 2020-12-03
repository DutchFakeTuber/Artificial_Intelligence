from django.urls import path
from results_AI import views

urlpatterns = [
    path('', views.results, name='results')
]