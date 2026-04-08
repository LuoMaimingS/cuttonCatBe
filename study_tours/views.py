from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import StudyTour, StudyTourEnrollment
from .serializers import StudyTourSerializer, StudyTourEnrollmentSerializer

class StudyTourViewSet(viewsets.ModelViewSet):
    queryset = StudyTour.objects.all()
    serializer_class = StudyTourSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['title', 'location']
    ordering_fields = ['start_date', 'price', 'created_at']

class StudyTourEnrollmentViewSet(viewsets.ModelViewSet):
    queryset = StudyTourEnrollment.objects.all()
    serializer_class = StudyTourEnrollmentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['student_id', 'study_tour_id', 'status']
    ordering_fields = ['enroll_time', 'created_at']
