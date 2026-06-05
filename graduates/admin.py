from django.contrib import admin
from .models import Graduate, WorkExperience, Skill, Certification, AcademicProject, ProfileViewLog

class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1
    fields = ['job_title', 'company', 'start_date', 'end_date', 'is_current', 'description']

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3
    fields = ['name']

class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1
    fields = ['name', 'issuing_organization', 'issue_date', 'expiry_date', 'credential_url']

class AcademicProjectInline(admin.TabularInline):
    model = AcademicProject
    extra = 1
    fields = ['name', 'description', 'year', 'project_url', 'image']

@admin.register(Graduate)
class GraduateAdmin(admin.ModelAdmin):
    list_display = ['user', 'major', 'graduation_year', 'gpa', 'current_job_status', 'is_verified', 'profile_views']
    list_filter = ['graduation_year', 'major', 'current_job_status', 'is_verified']
    search_fields = ['user__first_name', 'user__last_name', 'user__username', 'university_id', 'major']
    readonly_fields = ['profile_views', 'created_at', 'updated_at']
    fieldsets = (
        ('معلومات المستخدم', {
            'fields': ('user', 'university_id', 'phone')
        }),
        ('المعلومات الأكاديمية', {
            'fields': ('graduation_year', 'gpa', 'major', 'minor')
        }),
        ('المعلومات المهنية', {
            'fields': ('current_job_status', 'current_job_title', 'current_company')
        }),
        ('الملف الشخصي', {
            'fields': ('bio', 'profile_picture', 'cv_file')
        }),
        ('روابط التواصل', {
            'fields': ('linkedin_url', 'github_url')
        }),
        ('الحالة والإحصائيات', {
            'fields': ('is_verified', 'profile_views', 'reward_points', 'created_at', 'updated_at')
        }),
    )
    inlines = [WorkExperienceInline, SkillInline, CertificationInline, AcademicProjectInline]

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['graduate', 'job_title', 'company', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'company']
    search_fields = ['job_title', 'company', 'graduate__user__first_name']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['graduate', 'name']
    list_filter = ['name']
    search_fields = ['name', 'graduate__user__first_name']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['graduate', 'name', 'issuing_organization', 'issue_date']
    list_filter = ['issuing_organization']
    search_fields = ['name', 'issuing_organization']

@admin.register(AcademicProject)
class AcademicProjectAdmin(admin.ModelAdmin):
    list_display = ['graduate', 'name', 'year']
    list_filter = ['year']
    search_fields = ['name', 'graduate__user__first_name']

@admin.register(ProfileViewLog)
class ProfileViewLogAdmin(admin.ModelAdmin):
    list_display = ['graduate', 'viewer_user', 'viewer_ip', 'viewed_at']
    list_filter = ['viewed_at']
    readonly_fields = ['viewed_at']