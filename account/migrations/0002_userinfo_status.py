# Generated by Django 2.1.8 on 2021-06-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='status',
            field=models.TextField(blank=True, default='ok', help_text='帐号状态', verbose_name='状态'),
        ),
    ]