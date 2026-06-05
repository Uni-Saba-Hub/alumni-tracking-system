from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='كلمة المرور')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='تأكيد كلمة المرور')
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password']
        labels = {
            'username': 'اسم المستخدم',
            'first_name': 'الاسم الكامل',
            'email': 'البريد الإلكتروني',
        }
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('اسم المستخدم موجود بالفعل')
        return username
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('كلمة المرور غير متطابقة')
        
        if password and len(password) < 4:
            raise forms.ValidationError('كلمة المرور يجب أن تكون 4 أحرف على الأقل')
        
        return cleaned_data
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user