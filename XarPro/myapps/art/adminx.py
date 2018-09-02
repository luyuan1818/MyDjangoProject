import xadmin

# Register your models here.
from art.models import Tag, Category, Art, RollSet, Chapter
from xadmin import views


class BaseSetting:
    enable_themes = True
    use_bootswatch = True

class GlobalSetting:
    site_title = '玉龙中文网'
    site_footer = '大中华区西北联合服务部<h5>联系方式:15051332561</h5>'
    menu_style = 'accordion'
    global_models_icon = {
        Tag:'glyphicon glyphicon-tag',
        Category:'glyphicon glyphicon-th-large',
        Art:'glyphicon glyphicon-book',
        RollSet:'glyphicon glyphicon-pencil',
        Chapter:'glyphicon glyphicon-file',

    }
    apps_label_title = {
        'art':'文章管理'
    }
    apps_icons = {
        'art':'glyphicon glyphicon-star'
    }


xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSetting)
#--------------------后台管理添加Tag-------------------------
class TagAdmin:
    list_display = ('name', 'describe', 'add_time')
    list_per_page = 10  # 每页显示的记录数
    list_filter = ('add_time',)  # 过滤字段-查询数据的条件
    search_fields = ('name', 'describe')  # 搜索字段

xadmin.site.register(Tag,TagAdmin)
#--------------------后台管理添加Category-------------------------
class CategoryAdmin:
    list_display = ('title', 'parent', 'add_time')
    list_per_page = 10  # 每页显示的记录数
    list_filter = ('add_time',)  # 过滤字段-查询数据的条件
    search_fields = ('title', 'parent')  # 搜索字段

xadmin.site.register(Category,CategoryAdmin)
#--------------------后台管理添加Art-------------------------
class ArtAdmin:
    list_display = ('title', 'summary', 'content','author','publish_date','cover')
    list_per_page = 10  # 每页显示的记录数
    list_filter = ('publish_date',)  # 过滤字段-查询数据的条件
    search_fields = ('title', 'author')  # 搜索字段


xadmin.site.register(Art,ArtAdmin)
#---------------------------------------------
class RollSetAdmin:
    list_display = ('name', 'free_level', 'art')
    list_per_page = 10  # 每页显示的记录数
    #list_filter = ('publish_date',)  # 过滤字段-查询数据的条件
    search_fields = ('name', 'free_level')  # 搜索字段

xadmin.site.register(RollSet,RollSetAdmin)
#--------------------后台管理添加Art-------------------------
class ChapterAdmin:
    list_display = ('name', 'content', 'publish_date')
    list_per_page = 10  # 每页显示的记录数
    list_filter = ('publish_date',)  # 过滤字段-查询数据的条件
    search_fields = ('name', 'content')  # 搜索字段
    style_fields = {
        'content':'ueditor'
    }
xadmin.site.register(Chapter,ChapterAdmin)
#---------------------------------------------
#---------------------------------------------
#---------------------------------------------
