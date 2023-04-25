from django.contrib import admin
from .models import Site,Asin,Staff,Department,Post,Shop

class Site_Manager(admin.ModelAdmin):
    list_display = ['site','front_host','back_host','zip_code','create_date','update_date']
    # 增加自定义按钮
    actions = ['custom_button']

    def custom_button(self, request, queryset):
        print(queryset)

    # 添加按钮弹窗
    custom_button.confirm = '删库跑路？'
    # 按钮显示名称
    custom_button.short_description = '测试'

    # 图标，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'
    # # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'
    # # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

admin.site.register(Site,Site_Manager)


class Asin_Manager(admin.ModelAdmin):
    list_display = ['asin', 'site', 'status', 'shop', 'staff', 'create_date','update_date']

admin.site.register(Asin, Asin_Manager)

class Staff_Manager(admin.ModelAdmin):
    list_display = ['nick', 'name', 'mobile', 'dingding_key', 'gender', 'start_date','depart','post','create_date','update_date']

admin.site.register(Staff, Staff_Manager)

class Department_Manager(admin.ModelAdmin):
    list_display = ['id','title']

admin.site.register(Department, Department_Manager)

class Post_Manager(admin.ModelAdmin):
    list_display = ['title', 'level']

admin.site.register(Post, Post_Manager)

class Shop_Manager(admin.ModelAdmin):
    list_display = ['title', 'sever_ip','create_date','update_date']

admin.site.register(Shop, Shop_Manager)





# Register your models here.
admin.site.site_header = '亚马逊爬虫管理后台'  # 设置header
admin.site.site_title = '亚马逊爬虫管理后台'   # 设置title
admin.site.index_title = '亚马逊爬虫管理后台'






