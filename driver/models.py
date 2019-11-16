from django.db import models
from django.utils import timezone


GENDER_CHOICES = [
    ('1', '男性'),
    ('2', '女性'),
]


class Course(models.Model):
    name = models.CharField('コース', max_length=255)
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name

        
class Company(models.Model):
    name = models.CharField('会社名', max_length=255, default='ティートレジャー')
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return self.name


class Driver(models.Model):
    name = models.CharField('名前', max_length=20)
    age = models.IntegerField('年齢', blank=True)
    gender = models.CharField("性別", max_length=2, choices=GENDER_CHOICES, blank=True)
    phone = models.CharField("電話番号", max_length=255, blank=True)
    course = models.ManyToManyField(
        Course, verbose_name='コース'
    )
    company = models.ForeignKey(
        Company, verbose_name='会社名', on_delete=models.PROTECT, default='T'
    )
    created_at = models.DateTimeField('日付', default=timezone.now)

    def __str__(self):
        return f'{self.name}　 電話番号：{self.phone}'


