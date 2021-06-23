# Generated by Django 2.1.8 on 2021-06-23 06:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=65, verbose_name='余额')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='绑定用户')),
            ],
            options={
                'verbose_name_plural': '资金帐户',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.CharField(max_length=32, verbose_name='支出方')),
                ('to_user', models.CharField(max_length=32, verbose_name='接收方')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=65, verbose_name='交易金额')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=65, verbose_name='余额')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='时间')),
                ('type', models.IntegerField(choices=[(0, '收入'), (1, '支出')], verbose_name='类型')),
            ],
            options={
                'verbose_name_plural': '收支记录',
            },
        ),
        migrations.CreateModel(
            name='TransType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='其他', help_text='交易分类说明', max_length=128, verbose_name='名称')),
            ],
            options={
                'verbose_name_plural': '收支项',
            },
        ),
        migrations.AddField(
            model_name='transaction',
            name='trans_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finance.TransType'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]