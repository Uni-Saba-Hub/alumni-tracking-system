# -*- coding: utf-8 -*- 
from django.db import models 
from django.contrib.auth.models import User 
 
class Graduate(models.Model): 
    JOB_STATUS_CHOICES = [ 
        ('working', 'Working'), 
        ('seeking', 'Seeking Job'), 
        ('studying', 'Postgraduate'), 
        ('intern', 'Intern'), 
        ('entrepreneur', 'Entrepreneur'), 
    ] 
 
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='graduate_profile') 
    university_id = models.CharField("University ID", max_length=20, unique=True) 
    graduation_year = models.IntegerField("Graduation Year") 
    gpa = models.DecimalField("GPA", max_digits=3, decimal_places=2, null=True, blank=True) 
    major = models.CharField("Major", max_length=100) 
    minor = models.CharField("Minor", max_length=100, blank=True, null=True) 
    bio = models.TextField("Bio", blank=True, null=True) 
    current_job_status = models.CharField("Job Status", max_length=20, choices=JOB_STATUS_CHOICES, default='seeking') 
    current_job_title = models.CharField("Current Job Title", max_length=100, blank=True, null=True) 
    current_company = models.CharField("Current Company", max_length=100, blank=True, null=True) 
    cv_file = models.FileField("CV", upload_to='cvs/', blank=True, null=True) 
    profile_picture = models.ImageField("Profile Picture", upload_to='profiles/', blank=True, null=True) 
    linkedin_url = models.URLField(blank=True, null=True) 
    github_url = models.URLField(blank=True, null=True) 
    phone = models.CharField("Phone", max_length=15, blank=True, null=True) 
    is_verified = models.BooleanField("Verified", default=False) 
    profile_views = models.IntegerField("Profile Views", default=0) 
    created_at = models.DateTimeField("Registered", auto_now_add=True) 
    updated_at = models.DateTimeField("Last Update", auto_now=True) 
 
    def __str__(self): 
        return self.user.get_full_name() or self.user.username 
