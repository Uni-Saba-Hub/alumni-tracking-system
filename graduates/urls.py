from django.urls import path
from . import views

urlpatterns = [
    path('', views.graduate_list, name='graduate_list'),
]