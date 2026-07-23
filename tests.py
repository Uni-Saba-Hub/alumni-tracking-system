"""
اختبارات شاملة لنظام متابعة الخريجين
تشغيل: python manage.py test
"""

import os
import django
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

# ============================================================
# اختبارات تطبيق accounts (تسجيل الدخول والتسجيل)
# ============================================================
class AccountsTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='TestPass123'
        )
    
    def test_login_page_status(self):
        """صفحة تسجيل الدخول تعمل"""
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)
    
    def test_register_page_status(self):
        """صفحة التسجيل تعمل"""
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
    
    def test_login_with_valid_user(self):
        """تسجيل الدخول بمستخدم صحيح"""
        response = self.client.post(reverse('account_login'), {
            'login': 'testuser',
            'password': 'TestPass123'
        })
        self.assertIn(response.status_code, [200, 302])
    
    def test_login_with_invalid_user(self):
        """تسجيل الدخول بمستخدم غير صحيح"""
        response = self.client.post(reverse('account_login'), {
            'login': 'wronguser',
            'password': 'wrongpass'
        })
        self.assertEqual(response.status_code, 200)


# ============================================================
# اختبارات تطبيق graduates (الخريجين)
# ============================================================
class GraduatesTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='graduser',
            password='TestPass123'
        )
        from graduates.models import Graduate
        self.graduate = Graduate.objects.create(
            user=self.user,
            major='علوم حاسب',
            graduation_year=2024,
            is_verified=True
        )
    
    def test_graduate_list_page(self):
        response = self.client.get(reverse('graduate_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_graduate_model_created(self):
        from graduates.models import Graduate
        self.assertEqual(Graduate.objects.count(), 1)


# ============================================================
# اختبارات تطبيق employers (الشركات)
# ============================================================
class EmployersTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='empuser',
            password='TestPass123'
        )
        from employers.models import Employer
        self.employer = Employer.objects.create(
            user=self.user,
            company_name='شركة التقنية',
            is_verified=True
        )
    
    def test_employer_list_page(self):
        response = self.client.get(reverse('employer_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_employer_model_created(self):
        from employers.models import Employer
        self.assertEqual(Employer.objects.count(), 1)


# ============================================================
# اختبارات تطبيق jobs (الوظائف)
# ============================================================
class JobsTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        
        from employers.models import Employer
        from graduates.models import Graduate
        from jobs.models import Job
        
        self.user_emp = User.objects.create_user(
            username='emp_job',
            password='pass123'
        )
        self.employer = Employer.objects.create(
            user=self.user_emp,
            company_name='شركة البرمجة',
            is_verified=True
        )
        
        self.user_grad = User.objects.create_user(
            username='grad_job',
            password='pass123'
        )
        self.graduate = Graduate.objects.create(
            user=self.user_grad,
            major='هندسة برمجيات',
            graduation_year=2024
        )
        
        self.job = Job.objects.create(
            employer=self.employer,
            title='مطور ويب',
            location='عن بُعد',
            job_type='remote',
            is_active=True,
            deadline=timezone.now() + timedelta(days=30),
            description='مطلوب مطور ويب محترف'
        )
    
    def test_job_list_page(self):
        response = self.client.get(reverse('jobs:job_list'))
        self.assertEqual(response.status_code, 200)
    
    def test_job_detail_page(self):
        response = self.client.get(reverse('jobs:job_detail', args=[self.job.id]))
        self.assertEqual(response.status_code, 200)
    
    def test_job_application_creation(self):
        from jobs.models import JobApplication
        application = JobApplication.objects.create(
            job=self.job,
            graduate=self.graduate,
            status='pending'
        )
        self.assertEqual(JobApplication.objects.count(), 1)
        self.assertEqual(application.status, 'pending')


# ============================================================
# اختبارات تطبيق dashboard (لوحة التحكم)
# ============================================================
class DashboardTests(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username='admin_test',
            password='adminpass'
        )
        self.client.login(username='admin_test', password='adminpass')
    
    def test_dashboard_page(self):
        response = self.client.get(reverse('dashboard:admin_dashboard'))
        self.assertEqual(response.status_code, 200)
    
    def test_dashboard_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('dashboard:admin_dashboard'))
        # يجب أن يعيد التوجيه إلى صفحة تسجيل الدخول
        self.assertNotEqual(response.status_code, 200)


# ============================================================
# اختبارات عامة
# ============================================================
class GeneralTests(TestCase):
    
    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)