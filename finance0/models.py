from django.db import models
from django.contrib.auth.models import User


class Record(models.Model):
    user = models.ForeignKey(User, related_name="user_finance_record", on_delete=models.DO_NOTHING, blank=False)
    name = models.CharField(verbose_name='收支项', max_length=128, help_text='每一笔款项描述')
    money = models.DecimalField(verbose_name='金额', decimal_places=2, max_digits=9)
    remain = models.DecimalField(verbose_name='余额', decimal_places=2, max_digits=9)
    create_date = models.DateTimeField(verbose_name='时间', auto_now=True)

    type_choices = (
        (0, '收入'),
        (1, '支出'),
    )
    type = models.IntegerField(verbose_name='类型', choices=type_choices)

    class Meta:
        verbose_name = "收支"
        verbose_name_plural = "收支记录"

    def __str__(self):
        return self.name

class Account(models.Model):
    user = models.ForeignKey(User, related_name="user_finance_account", on_delete=models.DO_NOTHING, blank=False)
    balance = models.DecimalField(verbose_name='余额', decimal_places=2, max_digits=9)
    update_date = models.DateTimeField(verbose_name='时间', auto_now=True)


    class Meta:
        verbose_name = "结帐"


