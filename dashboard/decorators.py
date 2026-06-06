from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def super_admin_required(view_func):
    """فقط مدير النظام"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if hasattr(request.user, 'admin_profile') and request.user.admin_profile.admin_level == 'super_admin':
            return view_func(request, *args, **kwargs)
        messages.error(request, 'غير مصرح لك بالوصول إلى هذه الصفحة')
        return redirect('home')
    return wrapper


def alumni_manager_required(view_func):
    """مدير شؤون الخريجين أو أعلى"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if hasattr(request.user, 'admin_profile') and request.user.admin_profile.admin_level in ['super_admin', 'alumni_manager']:
            return view_func(request, *args, **kwargs)
        messages.error(request, 'غير مصرح لك بالوصول إلى هذه الصفحة')
        return redirect('home')
    return wrapper


def content_moderator_required(view_func):
    """مشرف محتوى أو أعلى"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if hasattr(request.user, 'admin_profile') and request.user.admin_profile.admin_level in ['super_admin', 'alumni_manager', 'content_moderator']:
            return view_func(request, *args, **kwargs)
        messages.error(request, 'غير مصرح لك بالوصول إلى هذه الصفحة')
        return redirect('home')
    return wrapper


def graduate_required(view_func):
    """فقط الخريجين"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if hasattr(request.user, 'graduate_profile'):
            return view_func(request, *args, **kwargs)
        messages.error(request, 'يجب أن تكون مسجلاً كخريج')
        return redirect('graduate_create')
    return wrapper


def employer_required(view_func):
    """فقط الشركات"""
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        if hasattr(request.user, 'employer_profile'):
            return view_func(request, *args, **kwargs)
        messages.error(request, 'يجب أن تكون مسجلاً كشركة')
        return redirect('employer_create')
    return wrapper


def owner_or_admin_required(model_class):
    """يسمح لصاحب الملف أو المشرف فقط"""
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            obj_id = kwargs.get('pk')
            obj = model_class.objects.get(pk=obj_id)
            
            # التحقق من أن المستخدم هو المالك
            if hasattr(obj, 'user') and request.user == obj.user:
                return view_func(request, *args, **kwargs)
            
            # أو أن المستخدم مشرف
            if hasattr(request.user, 'admin_profile'):
                return view_func(request, *args, **kwargs)
            
            messages.error(request, 'غير مصرح لك بتعديل هذا الملف')
            return redirect('home')
        return wrapper
    return decorator