# Generated by Django 2.1.8 on 2021-06-21 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='每一笔款项描述', max_length=128, verbose_name='收支项')),
                ('money', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='金额')),
                ('create_date', models.DateTimeField(auto_now=True, verbose_name='时间')),
                ('type', models.IntegerField(choices=[(0, '收入'), (1, '支出')], verbose_name='类型')),
            ],
            options={
                'verbose_name': '收支',
                'verbose_name_plural': '收支记录',
            },
        ),
    ]
