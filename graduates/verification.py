import re
from django.core.exceptions import ValidationError

def verify_university_id(university_id, graduation_year):
    """
    التحقق من صحة الرقم الجامعي
    الصيغة: يتكون من 8-10 أرقام ويحتوي على سنة التخرج
    """
    if not re.match(r'^\d{8,10}$', university_id):
        return False, "الرقم الجامعي يجب أن يكون 8-10 أرقام"
    
    # استخراج سنة التخرج من الرقم الجامعي (أول 4 أرقام أو آخر 4)
    year_from_id = int(str(university_id)[:4])
    
    if year_from_id != graduation_year:
        return False, f"سنة التخرج ({graduation_year}) لا تتطابق مع الرقم الجامعي ({year_from_id})"
    
    return True, "تم التحقق بنجاح"

def generate_verification_code():
    """إنشاء رمز تحقق عشوائي من 6 أرقام"""
    import random
    return str(random.randint(100000, 999999))