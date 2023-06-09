"""
Django settings for djangoProject1 project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
import app01.middleware.middleware

BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-r8u^-2nx#b#vyh5pe@%6q66ug@dzzatmswuivlar4_!muo33&r"






# Application definition

INSTALLED_APPS = [
    'simpleui',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'app01.apps.App01Config',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'app01.middleware.middleware.M1',
]

ROOT_URLCONF = "djangoProject1.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        #"DIRS": [BASE_DIR / 'templates']
        "DIRS": []
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "djangoProject1.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "amazon_data",  #数据库名字
        'USER': 'amazon_data',
        'PASSWORD': 'a00000000',
        'HOST': '106.13.1.144',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/





USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/



# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 指定simpleui默认的主题,指定一个文件名，相对路径就从simpleui的theme目录读取
# SIMPLEUI_DEFAULT_THEME = 'e-red-pro.less'
#是否开启默认图标
SIMPLEUI_DEFAULT_ICON = True
import time
# 自定义菜单
SIMPLEUI_CONFIG = {
    # 是否使用系统默认菜单，自定义菜单时建议关闭。
    'system_keep': False,
    # 用于菜单排序和过滤, 不填此字段为默认排序和全部显示。空列表[] 为全部不显示.
    'menu_display': ['需求管理', '账号管理', '爬虫管理', '维护管理','后台进程管理','作业流程',
                     '接口任务管理','任务结果','周期任务','短信管理','认证和授权','工具',],      # 开启排序和过滤功能, 不填此字段为默认排序和全部显示, 空列表[] 为全部不显示.
    'dynamic': True,    # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容  一般建议关闭。
    'menus': [
        {
        'name': '需求管理',
        'icon': 'fas fa-cog',
        # 'url': 'https://www.baidu.com',
        # 浏览器新标签中打开
        # 'newTab': True,
        'models': [{
            # 'app' : 'app01',
            'name': '站点管理',
            'icon': 'fa fa-user',
            'url': 'app01/site/'
        },{
            # 'app' : 'app01',
            'name': 'Asin管理',
            'icon': 'fa fa-user',
            'url': 'app01/asin/'
        },{
            # 'app' : 'app01',
            'name': '员工管理',
            'icon': 'fa fa-user',
            'url': 'app01/staff/'
        },{
            # 'app' : 'app01',
            'name': '部门管理',
            'icon': 'fa fa-user',
            'url': 'app01/department/'
        },{
            # 'app' : 'app01',
            'name': '岗位管理',
            'icon': 'fa fa-user',
            'url': 'app01/post/'
        },{
            # 'app' : 'app01',
            'name': '店铺管理',
            'icon': 'fa fa-user',
            'url': 'app01/shop/'
        }]
    },
        {
        'app': 'auth',
        'name': '账号管理',
        'icon': 'fas fa-stamp',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    },
        {
        'name': '爬虫管理',
        'icon': 'fas fa-spider',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    },
{
        'name': '维护管理',
        'icon': 'fas fa-hammer',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    },
{
        'name': '后台进程管理',
        'icon': 'fas fa-layer-group',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    },
{
        'name': '作业流程',
        'icon': 'fas fa-sitemap',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    },
{
        'name': '接口任务管理',
        'icon': 'fas fa-rectangle-list',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    },
{
        'name': '任务结果',
        'icon': 'fas fa-feather-pointed',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    },
{
        'name': '周期任务',
        'icon': 'fas fa-sliders',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    },
{
        'name': '短信管理',
        'icon': 'fas fa-square-envelope',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    },
{
        'name': '认证和授权',
        'icon': 'fas fa-shield-halved',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    },
{
        'name': '工具',
        'icon': 'fas fa-wrench',
        'models': [{
            'name': '用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        }]
    }]


    #     {
    #     # 自2021.02.01+ 支持多级菜单，models 为子菜单名
    #     'name': '多级菜单测试',
    #     'icon': 'fa fa-file',
    #   	# 二级菜单
    #     'models': [
    #         {
    #         'name': 'Baidu',
    #         'icon': 'far fa-surprise',
    #         # 第三级菜单 ，
    #         'models': [
    #             {
    #               'name': '爱奇艺',
    #               'url': 'https://www.iqiyi.com/dianshiju/'
    #               # 第四级就不支持了，element只支持了3级
    #             }, {
    #                 'name': '百度问答',
    #                 'icon': 'far fa-surprise',
    #                 'url': 'https://zhidao.baidu.com/'
    #             }
    #         ]
    #     },
    #         {
    #         'name': '内网穿透',
    #         'url': 'https://www.wezoz.com',
    #         'icon': 'fab fa-github'
    #     }]
    # },
    #     {
    #     'name': '动态菜单测试' ,
    #     'icon': 'fa fa-desktop',
    #     'models': [{
    #         'name': time.time(),
    #         'url': 'http://baidu.com',
    #         'icon': 'far fa-surprise'
    #     }]
    # }]
}
# 服务器信息  隐藏：
SIMPLEUI_HOME_INFO = False

 # 更改默认语言为中文
LANGUAGE_CODE = 'zh-hans'

 # 更改时区为上海
TIME_ZONE = 'Asia/Shanghai'
DEBUG = True  # 开发模式为True，实际生产False
# ALLOWED_HOSTS = ['106.13.1.144','127.0.0.1']  # 开发模式为*，实际生产为真实IP或域名
ALLOWED_HOSTS = ['*']
import os
STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static"),    # 开发模式
# ]
STATIC_ROOT = os.path.join(BASE_DIR, "static")    # 生产模式


# django-celery  配置的部分
# Broker配置，使用Redis作为消息中间件
BROKER_URL = 'redis://106.13.1.144:6379/1'

# BACKEND配置，这里使用redis
CELERY_RESULT_BACKEND = 'redis://106.13.1.144:6379/1'

# 结果序列化方案
CELERY_RESULT_SERIALIZER = 'json'

# 任务结果过期时间，秒
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24

# 时区配置
CELERY_TIMEZONE = 'Asia/Shanghai'

# 指定导入的任务模块，可以指定多个
# CELERY_IMPORTS = (
#    'other_dir.tasks',
# )

# 由于开发过程中simpleui有限通过cdn进行页面渲染，一般情况下我们需要将其调整成本地资源方式，往往生产环境是无法连接外网的
SIMPLEUI_STATIC_OFFLINE = True # 离线模式