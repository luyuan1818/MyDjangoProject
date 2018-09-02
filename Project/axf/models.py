from django.db import models

# Create your models here.
class Wheel(models.Model):
    img = models.CharField(max_length=150,verbose_name='图片')
    name = models.CharField(max_length=20, verbose_name='名称')
    trackid = models.CharField(max_length=20, verbose_name='商品编号')
    isDwlete = models.NullBooleanField(default=False,blank=True,null=True, verbose_name='逻辑删除')
class Nav(models.Model):
    img = models.CharField(max_length=150, verbose_name='图片')
    name = models.CharField(max_length=20, verbose_name='名称')
    trackid = models.CharField(max_length=20, verbose_name='导航编号')
    isDwlete = models.NullBooleanField(default=False, blank=True, null=True, verbose_name='逻辑删除')