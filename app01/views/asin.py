from app01 import models
from django.shortcuts import render , redirect
'''
    asin表
    asin表：id，asin，关联的站点表数据，是否爬取状态，关联的店铺，关联的负责人运营，添加时间，更新时间
'''

# def depart_list(request):
#     '''部门列表'''
#     queryset = models.Department.objects.all()
#
#     return render(request,'depart_list.html',{'queryset':queryset})
#
# def depart_add(request):
#     '''添加部门'''
#     if request.method == 'GET':
#         return render(request, 'depart_add.html')
#     elif request.method == 'POST':
#         depart_title = request.POST.get('title')
#         print(depart_title)
#         models.Department.objects.create(title = depart_title)
#         return redirect('/depart/list')
#
# def depart_delete(request):
#     nid = request.GET.get('nid')
#     models.Department.objects.filter(id = nid).delete()
#     return redirect('/depart/list')
#
# def depart_edit(request,nid):
#     if request.method == "GET":
#         edit_obj = models.Department.objects.filter(id=nid).first()
#         return render(request,'depart_edit.html',{'edit_obj':edit_obj})
#     elif request.method == 'POST':
#         title = request.POST.get('title')
#         models.Department.objects.filter(id = nid).update(title = title)
#         return redirect('/depart/list')