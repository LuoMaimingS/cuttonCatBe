from rest_framework import serializers
from .models import StudyTour, StudyTourEnrollment

class StudyTourSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyTour
        fields = '__all__'

class StudyTourEnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    study_tour_title = serializers.SerializerMethodField()

    class Meta:
        model = StudyTourEnrollment
        fields = '__all__'

    def get_student_name(self, obj):
        from students.models import Student
        student = Student.objects.filter(id=obj.student_id).first()
        return student.name if student else None

    def get_study_tour_title(self, obj):
        tour = StudyTour.objects.filter(id=obj.study_tour_id).first()
        return tour.title if tour else None
