from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField("العنوان", max_length=200)
    description = models.TextField("الوصف", blank=True)
    date = models.DateTimeField("التاريخ")
    location = models.CharField("المكان", max_length=200)
    image = models.ImageField("صورة", upload_to='events/', blank=True, null=True)
    is_active = models.BooleanField("نشط", default=True)
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['date']

class StudyMaterial(models.Model):
    CATEGORY_CHOICES = [
        ('pdf', 'PDF'),
        ('video', 'فيديو'),
        ('doc', 'مستند'),
        ('link', 'رابط خارجي'),
    ]
    title = models.CharField("العنوان", max_length=200)
    description = models.TextField("الوصف", blank=True)
    category = models.CharField("النوع", max_length=20, choices=CATEGORY_CHOICES, default='pdf')
    file = models.FileField("الملف", upload_to='study/', blank=True, null=True)
    link = models.URLField("رابط", blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)
    
    def __str__(self):
        return self.title

class SuccessStory(models.Model):
    graduate_name = models.CharField("اسم الخريج", max_length=100)
    title = models.CharField("العنوان", max_length=200)
    content = models.TextField("القصة")
    image = models.ImageField("صورة", upload_to='stories/', blank=True, null=True)
    graduation_year = models.IntegerField("سنة التخرج")
    current_job = models.CharField("الوظيفة الحالية", max_length=100, blank=True)
    is_approved = models.BooleanField("موافق عليها", default=False)
    created_at = models.DateTimeField("تاريخ النشر", auto_now_add=True)
    
    def __str__(self):
        return f"{self.graduate_name} - {self.title}"