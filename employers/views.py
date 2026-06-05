from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from .models import Employer, EmployerVerificationRequest
from .forms import EmployerForm, EmployerVerificationForm
from jobs.models import Job, JobApplication

class EmployerListView(ListView):
    model = Employer
    template_name = 'employers/employer_list.html'
    context_object_name = 'employers'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Employer.objects.filter(is_active=True, is_verified=True)
        
        search = self.request.GET.get('search', '')
        if search:
            queryset = queryset.filter(
                Q(company_name__icontains=search) |
                Q(industry__icontains=search) |
                Q(headquarters__icontains=search)
            )
        
        industry = self.request.GET.get('industry', '')
        if industry:
            queryset = queryset.filter(industry=industry)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_companies'] = Employer.objects.filter(is_active=True).count()
        context['verified_companies'] = Employer.objects.filter(is_verified=True).count()
        return context


class EmployerDetailView(DetailView):
    model = Employer
    template_name = 'employers/employer_profile.html'
    context_object_name = 'employer'
    
    def get_object(self):
        obj = super().get_object()
        obj.views_count += 1
        obj.save()
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_jobs'] = self.object.jobs.filter(is_active=True, deadline__gte=timezone.now())
        context['total_applications'] = JobApplication.objects.filter(job__employer=self.object).count()
        return context


class EmployerCreateView(LoginRequiredMixin, CreateView):
    model = Employer
    form_class = EmployerForm
    template_name = 'employers/employer_form.html'
    success_url = reverse_lazy('employer_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, '✅ تم تسجيل الشركة بنجاح! سيتم مراجعة طلبك قريباً')
        return response


class EmployerUpdateView(LoginRequiredMixin, UpdateView):
    model = Employer
    form_class = EmployerForm
    template_name = 'employers/employer_form.html'
    success_url = reverse_lazy('employer_list')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '✅ تم تحديث بيانات الشركة بنجاح')
        return response


class EmployerDeleteView(LoginRequiredMixin, DeleteView):
    model = Employer
    success_url = reverse_lazy('employer_list')
    template_name = 'employers/employer_confirm_delete.html'
    
    def delete(self, request, *args, **kwargs):
        messages.success(request, '✅ تم حذف الشركة بنجاح')
        return super().delete(request, *args, **kwargs)


def verify_employer(request, pk):
    employer = get_object_or_404(Employer, pk=pk)
    
    if request.method == 'POST':
        form = EmployerVerificationForm(request.POST, request.FILES)
        if form.is_valid():
            verification = form.save(commit=False)
            verification.employer = employer
            verification.save()
            messages.success(request, '✅ تم إرسال طلب التوثيق بنجاح، سيتم مراجعته قريباً')
            return redirect('employer_profile', pk=employer.pk)
    else:
        form = EmployerVerificationForm()
    
    return render(request, 'employers/employer_verify.html', {'form': form, 'employer': employer})