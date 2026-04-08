from django.db import models
from core.models import TimeStampedModel

class StudyTour(TimeStampedModel):
    title = models.CharField(max_length=200, verbose_name="研学主题")
    description = models.TextField(verbose_name="详细介绍")
    start_date = models.DateField(verbose_name="开始日期")
    end_date = models.DateField(verbose_name="结束日期")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="费用")
    location = models.CharField(max_length=200, verbose_name="研学地点")

    class Meta:
        managed = False
        db_table = 'study_tour'
        verbose_name = "研学信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class StudyTourEnrollment(TimeStampedModel):
    student_id = models.BigIntegerField(verbose_name="学员ID", db_index=True)
    study_tour_id = models.BigIntegerField(verbose_name="研学活动ID", db_index=True)
    enroll_time = models.DateTimeField(auto_now_add=True, verbose_name="报名时间")
    status = models.CharField(max_length=20, choices=(('pending', '待确认'), ('confirmed', '已确认'), ('cancelled', '已取消')), default='pending', verbose_name="状态")

    class Meta:
        managed = False
        db_table = 'study_tour_enrollment'
        verbose_name = "研学报名"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"Student {self.student_id} - Tour {self.study_tour_id}"
