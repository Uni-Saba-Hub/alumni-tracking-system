from django.shortcuts import render
from django.http import HttpResponse
from .models import Graduate

def home(request):
    return render(request, 'index.html')

def graduate_list(request):
    graduates = Graduate.objects.all()
    return render(request, 'graduates/graduate_list.html', {'graduates': graduates})