from django.db import models
from django.contrib.auth.models import User


# Create your models here.


# 银行帐户
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    balance = models.DecimalField(max_digits=65, decimal_places=2, verbose_name='余额')


class Transaction(models.Model):
    name = models.CharField(verbose_name='收支项', max_length=128, help_text='每一笔款项描述')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=False)
    from_user = models.CharField(max_length=32, verbose_name='支出方', blank=False, null=False)
    to_user = models.CharField(max_length=32, verbose_name='接收方', blank=False, null=False)
    amount = models.DecimalField(max_digits=65, decimal_places=2, verbose_name='交易金额')
    balance = models.DecimalField(max_digits=65, decimal_places=2, verbose_name='余额')
    create_date = models.DateTimeField(verbose_name='时间', auto_now=True)

    type_choices = (
        (0, '收入'),
        (1, '支出'),
    )
    type = models.IntegerField(verbose_name='类型', choices=type_choices)

    class Meta:
        verbose_name = "收支"
        verbose_name_plural = "收支记录"
    def save(self, *args, **kwargs):
        super(Transaction, self).save()


