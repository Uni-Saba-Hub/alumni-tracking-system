from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployerListView.as_view(), name='employer_list'),
    path('<int:pk>/', views.EmployerDetailView.as_view(), name='employer_detail'),
]