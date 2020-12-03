from django.urls import path
from forms_AI import views

urlpatterns = [
    path('', views.index, name='survey')
]