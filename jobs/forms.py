from django import forms
from .models import Job, JobApplication

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = [
            'title', 'job_type', 'experience_level', 'location',
            'salary_min', 'salary_max', 'is_salary_negotiable',
            'required_skills', 'preferred_skills', 'description',
            'responsibilities', 'benefits', 'deadline'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'job_type': forms.Select(attrs={'class':'form-control'}),
            'experience_level': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'salary_min': forms.NumberInput(attrs={'class': 'form-control'}),
            'salary_max': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_salary_negotiable': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'required_skills': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'مثال: Python, Django, JavaScript'}),
            'preferred_skills': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'responsibilities': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'benefits': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }


class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['cover_letter', 'expected_salary']
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 4, 'class': 'form-control', 'placeholder': 'اكتب رسالة تعريفية عن نفسك...'}),
            'expected_salary': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'مثال: 5000'}),
        }