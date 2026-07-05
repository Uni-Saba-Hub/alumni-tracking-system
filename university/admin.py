from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Event, StudyMaterial, SuccessStory

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_active')
    list_filter = ('is_active', 'date')
    search_fields = ('title', 'location')

@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title',)

@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('graduate_name', 'title', 'is_approved', 'graduation_year')
    list_filter = ('is_approved', 'graduation_year')
    search_fields = ('graduate_name', 'title')