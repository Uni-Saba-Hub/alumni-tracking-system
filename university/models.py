from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    """نموذج الفعاليات الجامعية"""
    title = models.CharField("العنوان", max_length=200)
    description = models.TextField("الوصف")
    date = models.DateTimeField("التاريخ")
    location = models.CharField("المكان", max_length=200)
    is_upcoming = models.BooleanField("قادم", default=True)
    image = models.ImageField("صورة", upload_to='events/', blank=True, null=True)
    created_at = models.DateTimeField("تاريخ الإنشاء", auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "فعالية"
        verbose_name_plural = "الفعاليات"
        ordering = ['date']


class StudyMaterial(models.Model):
    """نموذج المواد الدراسية السابقة"""
    CATEGORY_CHOICES = [
        ('pdf', 'ملف PDF'),
        ('video', 'فيديو'),
        ('doc', 'مستند'),
        ('link', 'رابط خارجي'),
    ]
    title = models.CharField("العنوان", max_length=200)
    description = models.TextField("الوصف", blank=True, null=True)
    category = models.CharField("النوع", max_length=20, choices=CATEGORY_CHOICES, default='pdf')
    file = models.FileField("الملف", upload_to='study_materials/', blank=True, null=True)
    link = models.URLField("رابط خارجي", blank=True, null=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField("تاريخ الإضافة", auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "مادة دراسية"
        verbose_name_plural = "المواد الدراسية"
        ordering = ['-created_at']


class SuccessStory(models.Model):
    """نموذج قصص النجاح المرتبطة بالجامعة"""
    graduate_name = models.CharField("اسم الخريج", max_length=100)
    title = models.CharField("العنوان", max_length=200)
    content = models.TextField("القصة")
    image = models.ImageField("صورة", upload_to='success_stories/', blank=True, null=True)
    graduation_year = models.IntegerField("سنة التخرج")
    current_job = models.CharField("الوظيفة الحالية", max_length=100, blank=True, null=True)
    is_approved = models.BooleanField("موافق عليها", default=False)
    created_at = models.DateTimeField("تاريخ النشر", auto_now_add=True)
    
    def __str__(self):
        return f"{self.graduate_name} - {self.title}"
    
    class Meta:
        verbose_name = "قصة نجاح"
        verbose_name_plural = "قصص النجاح"
        ordering = ['-created_at']


class UniversityInfo(models.Model):
    """معلومات الجامعة"""
    name = models.CharField("اسم الجامعة", max_length=200, default="جامعة إقليم سبأ")
    description = models.TextField("الوصف")
    logo = models.ImageField("شعار الجامعة", upload_to='university/', blank=True, null=True)
    phone = models.CharField("الهاتف", max_length=20, blank=True, null=True)
    email = models.EmailField("البريد الإلكتروني", blank=True, null=True)
    address = models.TextField("العنوان", blank=True, null=True)
    website = models.URLField("الموقع الإلكتروني", blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "معلومات الجامعة"
        verbose_name_plural = "معلومات الجامعة"