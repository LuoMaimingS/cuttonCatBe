from django.contrib import admin
from .models import Course, CourseSchedule, CourseApplication

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'teacher', 'capacity', 'created_at')
    search_fields = ('name', 'teacher')

@admin.register(CourseSchedule)
class CourseScheduleAdmin(admin.ModelAdmin):
    list_display = ('course_id', 'date', 'start_time', 'end_time', 'location', 'created_at')
    list_filter = ('date', 'course_id')

@admin.register(CourseApplication)
class CourseApplicationAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'schedule_id', 'apply_time', 'status', 'created_at')
    list_filter = ('status', 'apply_time')
