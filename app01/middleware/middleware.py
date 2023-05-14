from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import render , redirect,HttpResponse
class M1(MiddlewareMixin):
    def process_request(self,request):
        #1.用户跳转到登录界面，无需验证session
        #获取当前请求路由
        current_path = request.path_info
        print(current_path)
        if current_path in ['/login/','/img/code/']:
            return None
        #如果方法中没有返回值，默认返回None就会继续往后走，如果有返回值，返回值得是跟视图函数一致的HttpResopnse,render,redirect
        # 2.用户跳转到非登录界面，验证session，已登录的话就继续（默认return None,也可以不写），未登录需要跳转登录界面
        info = request.session.get('info')
        if not info:
            return redirect('/login')


    def process_response(self,request,response):
        print('M1出去了')
        return response


class M2(MiddlewareMixin):
    def process_request(self, request):
        print('M2进来了')

    def process_response(self, request, response):
        print('M2出去了')
        return response