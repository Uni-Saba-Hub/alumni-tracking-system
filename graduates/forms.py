from django import forms
from .models import Graduate

class GraduateForm(forms.ModelForm):
    gpa = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'مثال: 88.50 أو 3.75 أو 55.88'}),
        help_text='يمكنك إدخال المعدل بصيغة 55 أو 55.8 أو 55.88'
    )
    
    class Meta:
        model = Graduate
        fields = [
            'university_id', 'graduation_year', 'gpa', 'major', 'minor',
            'bio', 'current_job_status', 'current_job_title', 'current_company',
            'cv_file', 'profile_picture', 'linkedin_url', 'github_url', 'phone'
        ]
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control', 'min': 1980, 'max': 2030}),
            'university_id': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '777123456'}),
            'major': forms.TextInput(attrs={'class': 'form-control'}),
            'minor': forms.TextInput(attrs={'class': 'form-control'}),
            'current_job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'current_company': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://linkedin.com/in/username'}),
            'github_url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'https://github.com/username'}),
        }
    
    def clean_gpa(self):
        gpa = self.cleaned_data.get('gpa')
        if gpa:
            gpa = gpa.strip().replace('،', '.')
            
            import re
            if not re.match(r'^\d+(\.\d{1,2})?$', gpa):
                raise forms.ValidationError('❌ صيغة المعدل غير صحيحة. استخدم أرقاماً فقط مثل: 55 أو 55.8 أو 55.88')
            
            try:
                value = float(gpa)
                if value > 1000:
                    raise forms.ValidationError('❌ المعدل كبير جداً. أدخل قيمة معقولة')
            except:
                raise forms.ValidationError('❌ أدخل رقماً صحيحاً')
        return gpa
    
    def clean_university_id(self):
        university_id = self.cleaned_data.get('university_id')
        if university_id:
            if not university_id.isdigit():
                raise forms.ValidationError('❌ الرقم الجامعي يجب أن يتكون من أرقام فقط')
            if len(university_id) < 8 or len(university_id) > 12:
                raise forms.ValidationError('❌ الرقم الجامعي يجب أن يكون بين 8 و 12 رقم')
        return university_id
    
    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            if not phone.isdigit():
                raise forms.ValidationError('❌ رقم الجوال يجب أن يتكون من أرقام فقط')
            if len(phone) < 9 or len(phone) > 12:
                raise forms.ValidationError('❌ رقم الجوال يجب أن يكون بين 9 و 12 رقم')
        return phone


class VerificationForm(forms.Form):
    university_id = forms.CharField(
        max_length=20, 
        label="الرقم الجامعي",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الرقم الجامعي'})
    )
    full_name = forms.CharField(
        max_length=100, 
        label="الاسم الكامل",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل اسمك كاملاً'})
    )
    graduation_year = forms.IntegerField(
        label="سنة التخرج",
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'مثال: 2025'})
    )