from app01 import models
from django.shortcuts import render , redirect,HttpResponse
from djangoProject1.tasks import *
from django.http import JsonResponse
from django import forms
from app01.utils.BootStrapModel import BootStrapForm,BootStrapModelForm
from app01.utils.code import check_code
from app01.utils.encrypt_dj import calc_md5
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
import json



def task_add_view(request):
    result = add.delay(100, 200)
    return HttpResponse(f'执行add任务的结果是{result}')


from celery import result
def get_result_by_taskid(request):
    task_id = request.GET.get('task_id')
    # 异步执行
    ar = result.AsyncResult(task_id)

    if ar.ready():
        return JsonResponse({'status': ar.state, 'result': ar.get()})
    else:

        return JsonResponse({'status': ar.state, 'result': ''})


def index(request):
    return HttpResponse('index页面')

def admin_list(request):
    '''管理员列表'''

    return HttpResponse('admin_list页面')


class LoginForm(BootStrapForm):
    username = forms.CharField(label='用户名',max_length=32,
                               widget=forms.TextInput(),required=True)
    password = forms.CharField(label='密码',max_length=64,
                               widget=forms.PasswordInput(render_value=True),required=True)
    code = forms.CharField(label='验证码',max_length=32,
                               widget=forms.TextInput(),required=True)
    def clean_password(self):
        #django 默认密码加密方式是pbkdf_sha256加密，可以使用set_password进行加密
        password = calc_md5(self.cleaned_data.get('password'))
        return password


def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,"login.html", {"form":form})
    form = LoginForm(data = request.POST)
    if form.is_valid():
        # 验证成功 获取到的用户名密码
        print(form.cleaned_data)
        user_input_code = form.cleaned_data.pop("code")#这里需要是pop，因为数据库里只有用户名密码，没有code
        code = request.session.get('image_code','')#超时60秒会报错，所以要设个空值
        if code.upper() != user_input_code.upper():
            form.add_error('code',"验证码错误")
            return render(request,'login.html',{'form':form})

        print(models.Admin.objects.filter(**form.cleaned_data))
        result = models.Admin.objects.filter(**form.cleaned_data).first()
        if not result:
            print('用户名或密码错误')
            form.add_error("password","用户名或密码不正确")
            return render(request, 'login.html', {'form':form})
        # 用户名密码正确
        # 网站生成随机字符串，写到用户浏览器的cookie中，再写入到session中
        request.session['info'] = {'id':result.id,'username':result.username}
        #session可以保存7天
        request.session.set_expiry(60*60*24*7)
        return redirect('/admin_list/')
    else:
        return render(request, "login.html", {"form": form})


def logout(request):
    # 注销登录
    request.session.clear()
    return redirect("/login/")

def img_code(request):
    img,img_str = check_code(font_file=r'\app01\static\font\kumo.ttf',project_name='SimpleUI-Test')
    print(img_str)
    #将验证码存入session中
    request.session['image_code'] = img_str
    request.session.set_expiry(60)  #设置超时时间60s
    stream = BytesIO()
    img.save(stream, 'png')
    return HttpResponse(stream.getvalue(),content_type="image/png")



@csrf_exempt
def task_ajax(request):
    # print(request.GET)
    # print(request.POST)
    data_dict = {'status':True,"data":[11,22,33,44]}
    json_string = json.dumps(data_dict)
    return HttpResponse(json_string)
    # return JsonResponse(data_dict) #等价于上面

class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = '__all__'
        widgets = {
            'detail':forms.TextInput
        }

def task_list(request):
    '''任务列表'''
    form = TaskModelForm()
    return render(request,"task_list.html",{'form':form})

@csrf_exempt
def task_add(request):
    '''添加任务'''
    print(request.POST)
    #对用户发送来的数据进行校验  利用ModelForm进行校验
    form = TaskModelForm(data = request.POST)
    if form.is_valid():
        form.save()
        data_dict = {'status': True}
        json_string = json.dumps(data_dict)
        return HttpResponse(json_string)
    data_dict = {'status': False,'error':form.errors}
    json_string = json.dumps(data_dict,ensure_ascii=False)
    return HttpResponse(json_string)


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        fields = '__all__'


@csrf_exempt
def order_list(request):
    '''订单管理'''
    form = OrderModelForm()
    return render(request,'order_list.html',{'form':form})



