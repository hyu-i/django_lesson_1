# Generated by Django 2.2.6 on 2019-11-02 13:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='ティートレジャー', max_length=255, verbose_name='会社名')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='コース')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='名前')),
                ('age', models.IntegerField(blank=True, verbose_name='年齢')),
                ('gender', models.CharField(blank=True, choices=[('1', '男性'), ('2', '女性')], max_length=2, verbose_name='性別')),
                ('phone', models.CharField(blank=True, max_length=255, verbose_name='電話番号')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
                ('company', models.ForeignKey(default='T', on_delete=django.db.models.deletion.PROTECT, to='driver.Company', verbose_name='会社名')),
                ('course', models.ManyToManyField(to='driver.Course', verbose_name='コース')),
            ],
        ),
    ]
