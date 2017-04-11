from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class MyUser(models.Model):
    school=models.CharField(max_length=50, blank=True, null=True, verbose_name='学校')
    qq = models.CharField(max_length=20, blank=True, null=True, verbose_name='QQ号码')
    mobile = models.CharField(max_length=11, blank=True, null=True, unique=True, verbose_name='手机号码')
    user = models.ForeignKey(User)
    class Meta:
        verbose_name = '普通用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.user.get_username()
class Group_info(models.Model):
    subject = models.CharField(max_length=50)
    class_info = models.TextField()
    teacher = models.CharField(max_length=50)
    teacher_info =models.TextField()
    groups_info = models.ManyToManyField(User,blank=True)
    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name
class Suggestion(models.Model):
    suggestion=models.TextField()
    class Meta:
        verbose_name = '建议'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.suggestion