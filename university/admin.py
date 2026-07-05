from django.contrib import admin
from .models import Event, StudyMaterial, SuccessStory, UniversityInfo

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location', 'is_upcoming')
    list_filter = ('is_upcoming', 'date')
    search_fields = ('title', 'description')


@admin.register(StudyMaterial)
class StudyMaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    list_filter = ('category',)
    search_fields = ('title',)


@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('graduate_name', 'title', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'graduation_year')
    search_fields = ('graduate_name', 'title')


@admin.register(UniversityInfo)
class UniversityInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')