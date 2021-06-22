from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return 'user {}'.format(self.user.username)


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True) 
    school = models.CharField(max_length=100, blank=True)
    company = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    status = models.CharField(max_length=32, blank=True, default="ok", verbose_name='状态', help_text='帐号状态')
    employe_id = models.IntegerField(blank=True, default=0, verbose_name='工号', help_text='员工编号')
    
    def __str__(self):
        return "user:{}".format(self.user.username)
