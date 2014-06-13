#coding:utf-8

from django.db import models
from django.contrib.auth.models import AbstractUser

class LabMember(AbstractUser):
    YEAR_IN_SCHOOL_CHOICES = (
        (1, "学部1年"),
        (2, "学部2年"),
        (3, "学部3年"),
        (4, "学部4年"),
        (5, "修士1年"),
        (6, "修士2年"),
        (7, "博士1年"),
        (8, "博士2年"),
        (9, "博士3年"),
        (10, "教員"),
        (99, "その他"),
    )

    year_in_school = models.PositiveIntegerField("学年", choices = YEAR_IN_SCHOOL_CHOICES, default=4)
    
    class Meta:
        app_label = "accounts"
        # db_table = "auth_user"
        verbose_name = "ユーザ"
        verbose_name_plural = "ユーザ"