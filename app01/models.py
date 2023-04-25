from django.db import models

# Create your models here.

class Asin(models.Model):
    '''
    asin表
    asin表：id，asin，关联的站点表数据，是否爬取状态，关联的店铺，关联的负责人运营，添加时间，更新时间
    '''
    asin = models.CharField(verbose_name='Asin',max_length=32) #asin
    site = models.ForeignKey(on_delete=models.CASCADE,to = 'Site', to_field='id',verbose_name='站点')
    status_choices = (
        (1, '未爬取'),
        (2, '已成功爬取'),
        (3, '正在爬取'),
        (4, '爬取失败'),
    )
    status = models.SmallIntegerField(verbose_name='状态', choices=status_choices, default=1)
    shop = models.ForeignKey(on_delete=models.CASCADE, to='Shop', to_field='id',verbose_name='店铺')
    staff = models.ForeignKey(on_delete=models.CASCADE, to='Staff', to_field='id',verbose_name='员工')
    create_date = models.DateTimeField(verbose_name='添加时间')
    update_date = models.DateTimeField(verbose_name='更新时间')
    # id = models.AutoField(verbose_name='ID',primary_key=True)
    def __str__(self):
        return self.asin

class Staff(models.Model):
    '''
        员工表
        人员表：id，昵称，姓名，手机号，钉钉key，性别，入职时间，部门，岗位，添加时间，更新时间
    '''
    nick = models.CharField(verbose_name='昵称', max_length=32)
    name = models.CharField(verbose_name='姓名', max_length=32)
    mobile = models.CharField(verbose_name='手机号', max_length=32)
    dingding_key = models.CharField(verbose_name='钉钉key', max_length=32)
    gender_choices = (
        (1, '男'), (2, '女')
    )
    gender = models.SmallIntegerField(verbose_name='性别', choices=gender_choices)
    start_date = models.DateTimeField(verbose_name='入职时间')
    depart = models.ForeignKey(on_delete=models.CASCADE,to = 'Department', to_field='id',verbose_name='部门')
    post = models.ForeignKey(on_delete=models.CASCADE,to = 'Post', to_field='id',verbose_name ='岗位')
    create_date = models.DateTimeField(verbose_name='添加时间')
    update_date = models.DateTimeField(verbose_name='更新时间')
    def __str__(self):
        return self.name


class Department(models.Model):
    ''' 部门表'''
    title = models.CharField(verbose_name='部门名称',max_length=32)
    # id = models.AutoField(verbose_name='ID',primary_key=True)
    def __str__(self):
        return self.title

class Post(models.Model):
    ''' 岗位表'''
    title = models.CharField(verbose_name='岗位名称',max_length=32)
    level_choices = (
        (1, '1级'),
        (2, '2级'),
        (3, '3级'),
        (4, '4级'),
    )
    level = models.SmallIntegerField(verbose_name='级别', choices=level_choices, default=1)
    # id = models.AutoField(verbose_name='ID',primary_key=True)
    def __str__(self):
        return self.title

class Shop(models.Model):
    '''
    店铺表
    店铺表：id，店铺名称，店铺所在服务器的ip，添加时间，更新时间
    '''
    title = models.CharField(verbose_name='店铺名称', max_length=32)
    sever_ip = models.CharField(verbose_name='服务器IP', max_length=32)
    create_date = models.DateTimeField(verbose_name='添加时间')
    update_date = models.DateTimeField(verbose_name='更新时间')
    def __str__(self):
        return self.title


class Site(models.Model):
    '''
    站点表
    站点表：id，站点标识，前台host，后台host，邮编，添加时间，更新时间
    '''
    site_choices = (
        (1, 'de'), #德国
        (2, 'cn'), #中国
        (3, 'usa'), #美国
        (4, 'ca'), #加拿大
    )
    site = models.SmallIntegerField(verbose_name='站点', choices=site_choices, default=1)
    front_host = models.CharField(verbose_name='前台host', max_length=32)
    back_host = models.CharField(verbose_name='后台host', max_length=32)
    zip_code = models.CharField(verbose_name='邮编', max_length=32)
    create_date = models.DateTimeField(verbose_name='添加时间')
    update_date = models.DateTimeField(verbose_name='更新时间')

    class Meta:
        verbose_name = '站点表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.site_choices[self.site-1][1] + self.front_host


