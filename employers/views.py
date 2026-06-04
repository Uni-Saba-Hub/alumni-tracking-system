from django.views.generic import ListView, DetailView
from .models import Employer

class EmployerListView(ListView):
    model = Employer
    template_name = 'employers/employer_list.html'
    context_object_name = 'employers'

class EmployerDetailView(DetailView):
    model = Employer
    template_name = 'employers/employer_detail.html'
    context_object_name = 'employer'