# -*- coding: utf-8 -*- 
from django.db import models 
from employers.models import Employer 
from graduates.models import Graduate 
 
class Job(models.Model): 
    JOB_TYPE_CHOICES = [ 
        ('full_time', 'Full Time'), 
        ('part_time', 'Part Time'), 
        ('remote', 'Remote'), 
        ('internship', 'Internship'), 
    ] 
 
    employer = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='jobs') 
    title = models.CharField("Job Title", max_length=200) 
    job_type = models.CharField("Job Type", max_length=20, choices=JOB_TYPE_CHOICES) 
    location = models.CharField("Location", max_length=200) 
    salary_min = models.DecimalField("Min Salary", max_digits=10, decimal_places=2, null=True, blank=True) 
    salary_max = models.DecimalField("Max Salary", max_digits=10, decimal_places=2, null=True, blank=True) 
    is_salary_negotiable = models.BooleanField("Salary Negotiable", default=False) 
    required_skills = models.TextField("Required Skills") 
    description = models.TextField("Job Description") 
    deadline = models.DateField("Application Deadline") 
    is_active = models.BooleanField("Active", default=True) 
    is_filled = models.BooleanField("Filled", default=False) 
    created_at = models.DateTimeField("Posted", auto_now_add=True) 
 
    def __str__(self): 
        return f"{self.title} at {self.employer.company_name}" 
 
class JobApplication(models.Model): 
    STATUS_CHOICES = [ 
        ('pending', 'Pending'), 
        ('reviewed', 'Reviewed'), 
        ('interview', 'Interview'), 
        ('accepted', 'Accepted'), 
        ('rejected', 'Rejected'), 
        ('hired', 'Hired'), 
    ] 
 
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications') 
    graduate = models.ForeignKey(Graduate, on_delete=models.CASCADE, related_name='applications') 
    status = models.CharField("Status", max_length=20, choices=STATUS_CHOICES, default='pending') 
    applied_at = models.DateTimeField("Applied", auto_now_add=True) 
    reviewed_at = models.DateTimeField("Reviewed", null=True, blank=True) 
    employer_notes = models.TextField("Notes", blank=True, null=True) 
 
    class Meta: 
        unique_together = ('job', 'graduate') 
 
    def __str__(self): 
        return f"{self.graduate} applied for {self.job.title}" 
