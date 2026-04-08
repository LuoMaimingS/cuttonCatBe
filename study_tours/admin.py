from django.contrib import admin
from .models import StudyTour, StudyTourEnrollment

@admin.register(StudyTour)
class StudyTourAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'price', 'location', 'created_at')
    search_fields = ('title', 'location')

@admin.register(StudyTourEnrollment)
class StudyTourEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'study_tour_id', 'enroll_time', 'status', 'created_at')
    list_filter = ('status', 'enroll_time')
