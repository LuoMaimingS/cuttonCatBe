from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Course, CourseSchedule, CourseApplication
from .serializers import CourseSerializer, CourseScheduleSerializer, CourseApplicationSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'teacher']
    ordering_fields = ['created_at']

class CourseScheduleViewSet(viewsets.ModelViewSet):
    queryset = CourseSchedule.objects.all()
    serializer_class = CourseScheduleSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course_id', 'date']
    ordering_fields = ['date', 'start_time', 'created_at']

class CourseApplicationViewSet(viewsets.ModelViewSet):
    queryset = CourseApplication.objects.all()
    serializer_class = CourseApplicationSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['student_id', 'schedule_id', 'status']
    ordering_fields = ['apply_time', 'created_at']
