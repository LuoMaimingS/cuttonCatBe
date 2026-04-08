from django.db import models
from core.models import TimeStampedModel

class Student(TimeStampedModel):
    name = models.CharField(max_length=50, verbose_name="姓名")
    birth_date = models.DateField(verbose_name="出生日期", null=True)
    age = models.IntegerField(verbose_name="年龄", null=True) # 保留以便兼容
    parent_name = models.CharField(max_length=50, verbose_name="家长姓名")
    phone = models.CharField(max_length=20, verbose_name="联系电话")
    enrolled_date = models.DateField(auto_now_add=True, verbose_name="报名日期")
    status = models.CharField(max_length=20, choices=(('active', '在读'), ('inactive', '结课')), default='active', verbose_name="状态")
    account_id = models.BigIntegerField(verbose_name="关联账号ID", db_index=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
        verbose_name = "学员"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
