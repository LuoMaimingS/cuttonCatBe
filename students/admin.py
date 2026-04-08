from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'parent_name', 'phone', 'enrolled_date', 'status', 'created_at')
    search_fields = ('name', 'phone', 'parent_name')
    list_filter = ('status', 'enrolled_date')
