from django.urls import path
from . import views

urlpatterns = [
    path('', views.EmployerListView.as_view(), name='employer_list'),
    path('<int:pk>/', views.EmployerDetailView.as_view(), name='employer_profile'),
    path('create/', views.EmployerCreateView.as_view(), name='employer_create'),
    path('<int:pk>/update/', views.EmployerUpdateView.as_view(), name='employer_update'),
    path('<int:pk>/delete/', views.EmployerDeleteView.as_view(), name='employer_delete'),
    path('<int:pk>/verify/', views.verify_employer, name='employer_verify'),
]