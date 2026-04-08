from rest_framework import serializers
from .models import Course, CourseSchedule, CourseApplication

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseScheduleSerializer(serializers.ModelSerializer):
    course_name = serializers.SerializerMethodField()
    teacher = serializers.SerializerMethodField()

    class Meta:
        model = CourseSchedule
        fields = '__all__'

    def get_course_name(self, obj):
        course = Course.objects.filter(id=obj.course_id).first()
        return course.name if course else None

    def get_teacher(self, obj):
        course = Course.objects.filter(id=obj.course_id).first()
        return course.teacher if course else None

class CourseApplicationSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    course_name = serializers.SerializerMethodField()
    schedule_date = serializers.SerializerMethodField()

    class Meta:
        model = CourseApplication
        fields = '__all__'

    def get_student_name(self, obj):
        from students.models import Student
        student = Student.objects.filter(id=obj.student_id).first()
        return student.name if student else None

    def get_course_name(self, obj):
        schedule = CourseSchedule.objects.filter(id=obj.schedule_id).first()
        if schedule:
            course = Course.objects.filter(id=schedule.course_id).first()
            return course.name if course else None
        return None

    def get_schedule_date(self, obj):
        schedule = CourseSchedule.objects.filter(id=obj.schedule_id).first()
        return schedule.date if schedule else None
