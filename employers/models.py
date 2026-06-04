# -*- coding: utf-8 -*- 
from django.db import models 
from django.contrib.auth.models import User 
 
class Employer(models.Model): 
    INDUSTRY_CHOICES = [ 
        ('tech', 'Ta9nia'), 
        ('construction', 'Maqawalat'), 
        ('medical', 'Tebi'), 
        ('education', 'Ta3lemi'), 
        ('marketing', 'Tasweq'), 
        ('finance', 'Mali'), 
        ('other', 'Okhra'), 
    ] 
 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer_profile') 
    company_name = models.CharField("Company Name", max_length=200, unique=True) 
    industry = models.CharField("Industry", max_length=50, choices=INDUSTRY_CHOICES) 
    employee_count = models.CharField("Employees Count", max_length=50, blank=True, null=True) 
    founded_year = models.IntegerField("Founded Year", null=True, blank=True) 
    headquarters = models.CharField("Headquarters", max_length=200) 
    about = models.TextField("About") 
    website = models.URLField(blank=True, null=True) 
    logo = models.ImageField("Logo", upload_to='logos/', blank=True, null=True) 
    commercial_registration = models.CharField("Commercial Registration", max_length=50, unique=True, blank=True, null=True) 
    is_verified = models.BooleanField("Verified", default=False) 
    is_active = models.BooleanField("Active", default=True) 
    created_at = models.DateTimeField(auto_now_add=True) 
 
    def __str__(self): 
        return self.company_name 
