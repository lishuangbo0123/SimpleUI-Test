from app01 import models
from django.shortcuts import render , redirect,HttpResponse
from djangoProject1.tasks import *


# Create your views here.

def task_add_view(request):
    result = add.delay(100, 200)
    return HttpResponse(f'执行add任务的结果是{result}')


from celery import result


def get_result_by_taskid(request):
    task_id = request.GET.get('task_id')
    # 异步执行
    ar = result.AsyncResult(task_id)

    if ar.ready():
        return HttpResponse(f"响应数据是{'status': ar.state, 'result': ar.get()}")
    else:

        return HttpResponse(f"响应数据是{'status': ar.state, 'result': 'ar.ready()没取到'}")