from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    # ====== المصادقة (Authentication) ======
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='/accounts/login/',
        template_name='registration/logout.html',
        http_method_names=['get', 'post']
    ), name='logout'),
    path('register/', views.register_view, name='register'),
    
    # ====== الملف الشخصي ======
    path('profile/', views.profile_view, name='profile'),
    path('account/', views.account_view, name='account'),
    
    # ====== التسجيل المبسط ======
    path('simple-register/', views.simple_register, name='simple_register'),
    
    # ============================================================
    # ✅ التحقق عبر البريد الإلكتروني (Email Verification)
    # ============================================================
    path('verify/<int:user_id>/', views.verify_email_view, name='verify_email'),
    path('resend/<int:user_id>/', views.resend_verification_code, name='resend_verification'),
]