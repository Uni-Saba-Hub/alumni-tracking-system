from django import forms
from .models import Employer, EmployerVerificationRequest

class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = [
            'company_name', 'short_name', 'industry', 'employee_count',
            'founded_year', 'headquarters', 'about', 'website',
            'logo', 'cover_image', 'commercial_registration', 'tax_number',
            'phone', 'email', 'address', 'latitude', 'longitude'
        ]
        widgets = {
            'about': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'industry': forms.Select(attrs={'class': 'form-control'}),
            'employee_count': forms.Select(attrs={'class': 'form-control'}),
            'founded_year': forms.NumberInput(attrs={'class': 'form-control', 'min': 1900, 'max': 2026}),
            'headquarters': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'commercial_registration': forms.TextInput(attrs={'class': 'form-control'}),
            'tax_number': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.000001'}),
        }


class EmployerVerificationForm(forms.ModelForm):
    class Meta:
        model = EmployerVerificationRequest
        fields = ['commercial_registration_file', 'tax_certificate']
        widgets = {
            'commercial_registration_file': forms.FileInput(attrs={'class': 'form-control'}),
            'tax_certificate': forms.FileInput(attrs={'class': 'form-control'}),
        }