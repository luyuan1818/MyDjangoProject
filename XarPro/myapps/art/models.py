import os
import uuid

from django.db import models

# Create your models here.

#---------文章标签Tag--------------
from DjangoUeditor.models import UEditorField


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
class Category(models.Model):
    title = models.CharField(max_length=20,verbose_name='标题',unique=True)
    add_time = models.DateTimeField(auto_now_add=True,verbose_name='添加时间')
    parent = models.ForeignKey('self',verbose_name='所属分类',on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'a_category'
        verbose_name = '小说分类'
        verbose_name_plural = verbose_name
        ordering = ['-add_time']

#--------------定义文件保存路径---------------------
def save_file_path(instance,filename):
    new_file_name = str(uuid.uuid4()).replace('-','')+os.path.splitext(filename)[-1]
    return 'arts/{}'.format(new_file_name)

#--------------文章Art---------------------
class Art(models.Model):
    title = models.CharField(max_length=20,verbose_name='文章名',unique=True)
    summary = models.CharField(max_length=50,verbose_name='简洁描述')
    content = models.CharField(max_length=100,verbose_name='详细描述')
    author = models.CharField(max_length=20,verbose_name='作者',unique=True)
    publish_date = models.DateTimeField(auto_now_add=True,verbose_name='上传时间')
    cover = models.ImageField(verbose_name='封面',upload_to=save_file_path,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='分类名')
    tags = models.ManyToManyField(Tag,verbose_name='标签名')
    def __str__(self):
        return self.title
    class Meta:
        db_table = 'a_art'
        verbose_name = '所有文章'
        verbose_name_plural = verbose_name
        ordering = ['-publish_date']
#---------------卷集--------------------
class RollSet(models.Model):
    free_levels = ((1,'free'),(2,'vip'))
    name = models.CharField(max_length=20,verbose_name='卷集名称',unique=True)

    free_level = models.IntegerField(choices=free_levels,verbose_name='免费等级',default=1)

    art = models.ForeignKey(Art,on_delete=models.CASCADE,verbose_name='所属文章')

    @property
    def free_level_name(self):
        return self.free_levels[self.free_level][1]
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'a_roll'
        verbose_name = '所有卷集'
        verbose_name_plural = verbose_name
        ordering = ['id']
#-----------------章节---------------------
class Chapter(models.Model):
    name = models.CharField(max_length=50,verbose_name='章节名称'
                            ,unique=True)
    content = UEditorField(verbose_name='章节内容',width=800,height=1000,
                           imagePath='ueditor/art/images/',
                           toolbars='mini')#功能多少分为mini,normal,full
    publish_date =  models.DateTimeField(auto_now_add=True,verbose_name='上传时间')

    rool = models.ForeignKey(RollSet,on_delete=models.CASCADE,verbose_name='所属卷集')

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'a_chapter'
        verbose_name = '章节'
        verbose_name_plural = verbose_name
        ordering = ['publish_date']

#----------------待补充...-------------------
#--------------------------------------