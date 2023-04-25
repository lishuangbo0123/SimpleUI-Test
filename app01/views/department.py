from app01 import models
from django.shortcuts import render , redirect
from app01.utils.pagination import Pagination
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from app01.utils.BootStrapModel import BootStrapModelForm
# from app01.form.form import NumModelForm,NumEditModelForm
'''部门表   名称 '''


def depart_list(request):
    '''部门列表'''
    dict = {}
    search_data = request.GET.get('q','')
    if search_data:
        dict['depart__contains'] = search_data
    queryset = models.Department.objects.filter(**dict).order_by('id')
    page_object = Pagination(request,queryset)
    content ={
        'model_list': page_object.page_queryset,
        'search_data': search_data,
        'page_string': page_object.html()
    }
    return render(request,'depart_list.html',content)

# def num_add(request):
#     '''添加靓号'''
#     if request.method == 'GET':
#         form = NumModelForm()
#         return render(request,'num_add.html',{"form":form})
#     form = NumModelForm(data=request.POST)
#     if form.is_valid():
#         form.save()
#         print(form.cleaned_data)
#         return redirect('/num/list')
#     else:
#         print(form.errors)
#         return render(request,'num_add.html',{"form":form})
#
#
#
# def num_edit(request,nid):
#     '''编辑靓号'''
#     row_object = models.PrettyNum.objects.filter(id = nid).first()
#     if request.method == 'GET':
#         form = NumEditModelForm(instance=row_object)
#         return render(request,'num_edit.html',{'form':form})
#     form = NumEditModelForm(data=request.POST,instance=row_object)
#     if form.is_valid():
#         form.save()
#         return redirect('/num/list')
#     print(form.errors)
#     return render(request,'num_edit.html',{'form':form})
#
# def num_delete(request,nid):
#     models.PrettyNum.objects.filter(id = nid).delete()
#     return redirect('/num/list')