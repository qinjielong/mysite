from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TransType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name='名称', max_length=128, help_text='交易分类说明', default='其他', unique=True)
    
    class Meta:
        verbose_name_plural = "收支项"

    def __str__(self):
        return self.name



class Transaction(models.Model):
    trans_type = models.ForeignKey(TransType, on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=False, null=False)
    from_user = models.CharField(max_length=32, verbose_name='支出方', blank=False, null=False)
    to_user = models.CharField(max_length=32, verbose_name='接收方', blank=False, null=False)
    amount = models.DecimalField(max_digits=65, decimal_places=2, verbose_name='交易金额')
    balance = models.DecimalField(max_digits=65, decimal_places=2, verbose_name='交易后余额')
    create_date = models.DateTimeField(verbose_name='时间', auto_now=True)

    type_choices = (
        (0, '收入'),
        (1, '支出'),
    )
    type = models.IntegerField(verbose_name='类型', choices=type_choices)

    class Meta:
        verbose_name_plural = "收支记录" 
    def save(self): 
        super(Transaction, self).save()


# 银行帐户
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='绑定用户', blank=False, null=False)
    balance = models.DecimalField(max_digits=65, decimal_places=2, verbose_name='余额')

    class Meta:
        verbose_name_plural = "资金帐户"
    
    def __str__(self):
        return self.user.username
   
    def update_balance(self, transaction):
        if self.user != transaction.user:
            return False
	
        if (self.balance + transaction.amount < 0):
            print(self.balance)
            return False
        self.balance = self.balance + transaction.amount
        self.save();
        transaction.balance = self.balance
        transaction.save()
        return True

