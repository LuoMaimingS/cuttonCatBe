from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        abstract = True


class Account(TimeStampedModel):
    username = models.CharField(max_length=50, unique=True, verbose_name="用户名")
    password = models.CharField(max_length=128, verbose_name="密码")
    phone = models.CharField(max_length=20, verbose_name="手机号")

    class Meta:
        managed = False
        db_table = 'account'
        verbose_name = "账号"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
