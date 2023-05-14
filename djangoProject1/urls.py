"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01.view import task_add_view,get_result_by_taskid,index,admin_list,login,logout,img_code,task_list
from app01 import view
urlpatterns = [
    path("admin/", admin.site.urls),
    path("celery/", task_add_view),
    path("get_result_by_taskid/",get_result_by_taskid),
    path("index/",index),
    path('login/',login),

    #管理员
    path("admin_list/",admin_list),
    path("logout/",logout),
    path('img/code/',img_code),

    #任务管理
    path("task/list/",task_list),
    path("task/ajax/",view.task_ajax),
    path("task/add/",view.task_add),

    #订单管理
    path("order/list/", view.order_list),
    path("task/add/",view.task_add),
]
