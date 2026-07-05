from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, StudyMaterial, SuccessStory, UniversityInfo

@login_required
def university_hub(request):
    """الصفحة الرئيسية للجامعة"""
    events = Event.objects.filter(date__gte=timezone.now()).order_by('date')[:5]
    study_materials = StudyMaterial.objects.all().order_by('-created_at')[:5]
    success_stories = SuccessStory.objects.filter(is_approved=True).order_by('-created_at')[:5]
    
    try:
        university_info = UniversityInfo.objects.first()
    except:
        university_info = None
    
    context = {
        'events': events,
        'study_materials': study_materials,
        'success_stories': success_stories,
        'university_info': university_info,
    }
    return render(request, 'university/hub.html', context)


@login_required
def event_detail(request, pk):
    """تفاصيل الفعالية"""
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'university/event_detail.html', {'event': event})


@login_required
def study_material_detail(request, pk):
    """تفاصيل المادة الدراسية"""
    material = get_object_or_404(StudyMaterial, pk=pk)
    return render(request, 'university/study_material_detail.html', {'material': material})