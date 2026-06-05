import django_filters
from .models import Graduate

class GraduateFilter(django_filters.FilterSet):
    major = django_filters.CharFilter(lookup_expr='icontains')
    graduation_year = django_filters.NumberFilter()
    graduation_year_gt = django_filters.NumberFilter(field_name='graduation_year', lookup_expr='gte')
    graduation_year_lt = django_filters.NumberFilter(field_name='graduation_year', lookup_expr='lte')
    gpa_min = django_filters.NumberFilter(field_name='gpa', lookup_expr='gte')
    gpa_max = django_filters.NumberFilter(field_name='gpa', lookup_expr='lte')
    current_job_status = django_filters.ChoiceFilter(choices=Graduate.JOB_STATUS_CHOICES)
    
    class Meta:
        model = Graduate
        fields = ['major', 'graduation_year', 'gpa', 'current_job_status']