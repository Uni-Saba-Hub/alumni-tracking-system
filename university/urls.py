from django.urls import path
from . import views

app_name = 'university'

urlpatterns = [
    path('', views.university_hub, name='hub'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('material/<int:pk>/', views.study_material_detail, name='study_material_detail'),
]