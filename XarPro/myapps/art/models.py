from django.db import models

# Create your models here.

#---------文章标签Tag--------------
class Tag(models.Model):
    name = models.CharField(max_length=50,verbose_name='标签名称',unique=True)
    describe = models.CharField(max_length=100,verbose_name='描述')
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'a_tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        ordering = ['-add_time']
#-------------文章分类Category----------------------
#-----------------------------------
#-----------------------------------
#-----------------------------------
#-----------------------------------
#-----------------------------------