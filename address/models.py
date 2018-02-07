from django.db import models
# Create your models here.
class Address(models.Model):
    name = models.CharField('name', max_length=6, unique=True)
    gender = models.CharField('gender', choices=(('M', 'Male'), ('F', 'Female')), max_length=1)
    telphone = models.CharField('telephone_number', max_length=20)
    mobile = models.CharField('mobile_number', max_length=11)
    room = models.CharField('房间', max_length=10, default='')

    def __str__(self):
        return self.name