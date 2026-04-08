from django.db import models
from core.models import TimeStampedModel

class Course(TimeStampedModel):
    name = models.CharField(max_length=100, verbose_name="课程名称")
    description = models.TextField(blank=True, verbose_name="课程描述")
    teacher = models.CharField(max_length=50, verbose_name="授课教师")
    capacity = models.IntegerField(default=10, verbose_name="容量")

    class Meta:
        managed = False
        db_table = 'course'
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseSchedule(TimeStampedModel):
    course_id = models.BigIntegerField(verbose_name="课程ID", db_index=True)
    date = models.DateField(verbose_name="上课日期")
    start_time = models.TimeField(verbose_name="开始时间")
    end_time = models.TimeField(verbose_name="结束时间")
    location = models.CharField(max_length=100, verbose_name="上课地点")

    class Meta:
        managed = False
        db_table = 'course_schedule'
        verbose_name = "课程安排"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"Course {self.course_id} - {self.date} {self.start_time}"


class CourseApplication(TimeStampedModel):
    student_id = models.BigIntegerField(verbose_name="学员ID", db_index=True)
    schedule_id = models.BigIntegerField(verbose_name="排课ID", db_index=True)
    apply_time = models.DateTimeField(auto_now_add=True, verbose_name="申请时间")
    status = models.CharField(max_length=20, choices=(('pending', '待审核'), ('approved', '已通过'), ('rejected', '已拒绝')), default='pending', verbose_name="状态")

    class Meta:
        managed = False
        db_table = 'course_application'
        verbose_name = "课程申请"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"Student {self.student_id} - Schedule {self.schedule_id}"
