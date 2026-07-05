from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, StudyMaterial, SuccessStory

@login_required
def university_hub(request):
    events = Event.objects.filter(is_active=True).order_by('date')[:5]
    materials = StudyMaterial.objects.all().order_by('-created_at')[:5]
    stories = SuccessStory.objects.filter(is_approved=True).order_by('-created_at')[:3]
    
    context = {
        'events': events,
        'materials': materials,
        'stories': stories,
    }
    return render(request, 'university/hub.html', context)

@login_required
def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'university/event_detail.html', {'event': event})

@login_required
def study_material_detail(request, pk):
    material = get_object_or_404(StudyMaterial, pk=pk)
    return render(request, 'university/study_material_detail.html', {'material': material})