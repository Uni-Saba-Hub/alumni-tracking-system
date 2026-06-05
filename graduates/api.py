from rest_framework import serializers, viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Graduate, WorkExperience, Skill, Certification, AcademicProject
from django.contrib.auth.models import User

# ========== Serializers ==========
class GraduateSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Graduate
        fields = ['id', 'full_name', 'major', 'graduation_year', 'gpa', 
                  'current_job_status', 'profile_picture', 'is_verified', 'profile_views']
    
    def get_full_name(self, obj):
        return obj.user.get_full_name() or obj.user.username

class GraduateDetailSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    work_experiences = WorkExperienceSerializer(many=True, read_only=True)
    skills = serializers.StringRelatedField(many=True)
    certifications = CertificationSerializer(many=True, read_only=True)
    
    class Meta:
        model = Graduate
        fields = '__all__'
    
    def get_full_name(self, obj):
        return obj.user.get_full_name() or obj.user.username

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

# ========== Viewsets ==========
class GraduateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Graduate.objects.filter(is_verified=True)
    serializer_class = GraduateSerializer
    permission_classes = [permissions.AllowAny]
    
    @action(detail=True, methods=['get'])
    def details(self, request, pk=None):
        graduate = self.get_object()
        serializer = GraduateDetailSerializer(graduate)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def increment_view(self, request, pk=None):
        graduate = self.get_object()
        graduate.profile_views += 1
        graduate.save()
        return Response({'status': 'ok', 'views': graduate.profile_views})