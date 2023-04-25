'''
以后如需要使用分页组件，需要做以下几件事
def num_list(request):
    1、根据对象筛选自己的数据
    queryset = models.PrettyNum.objects.filter(**dict).order_by('-level')
    2.实例化分页对象
    page_object = Pagination(request,queryset)

    content ={
        'model_list': page_object.page_queryset, #分完页的数据
        'search_data': search_data,              #生成页码
        'page_string': page_object.html()
    }
    return render(request,'num_list.html',content)
在HTML页面中，如果想展示分页，则
    {% for obj in queryset %}
        {{obj.xx}}
    {% endfor %}

    <ul class="pagination">
        {{ page_string }}
    </ul>
'''

import math
from django.utils.safestring import mark_safe


class Pagination(object):

    def __init__(self, request, queryset, page_param='page', page_size=20, plus=2):
        '''

        :param request: 请求的对象
        :param queryset: 查询到的数据列表
        :param page_param: 在url中传递的获取分页的参数 例如 /num/list/?page=12
        :param page_size: 每页显示多少条数据
        :param plus:  页码前后显示的页数
        '''
        page = request.GET.get(page_param, '1')
        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict
        self.page_param = page_param
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size

        self.total_count = queryset.count()
        self.total_page_count = math.ceil(self.total_count / page_size)
        self.plus = plus

        if self.total_page_count <= 2 * plus + 1:
            # 总页数小于 2 * plus + 1 时 起始1 结束 总页数
            self.start = 1
            self.end = self.total_page_count
        else:
            if page <= plus:
                # 当前页数小于plus时 起始页是1结束页是2 * plus + 1
                self.start = 1
                self.end = 2 * plus + 1
            elif page + plus >= self.total_page_count:
                # 当当前页+plus大于总页数，结束页是总页数  起始页是总页数-2*plus
                self.start = self.total_page_count - 2 * plus
                self.end = self.total_page_count
            else:

                self.start = page - plus
                self.end = page + plus

        self.page_queryset = queryset[(self.page - 1)*page_size:self.page*page_size]

    def getquery_dict(self,page):
        self.query_dict.setlist(self.page_param,[page])
        return self.query_dict.urlencode()

    def html(self):
        # html数据字符串列表
        page_str_list = []
        # 首页
        first_page = f'<li><a href="?{self.getquery_dict(1)}" aria-label="首页"><span aria-hidden="true">首页</span></a></li>'
        page_str_list.append(first_page)
        # 上一页
        if self.page > 1:
            prev = f'<li><a href="?{self.getquery_dict(self.page - 1)}" aria-label="上一页"><span aria-hidden="true">上一页</span></a></li>'
        else:
            prev = f'<li><a href="?{self.getquery_dict(1)}" aria-label="上一页"><span aria-hidden="true">上一页</span></a></li>'
        page_str_list.append(prev)

        for i in range(self.start, self.end + 1):
            if i == self.page:
                ele = f'<li class = "active"><a href="?{self.getquery_dict(i)}">{i}</a></li>'
            else:
                ele = f'<li><a href="?{self.getquery_dict(i)}">{i}</a></li>'
            page_str_list.append(ele)

        # 下一页
        if self.page == self.total_page_count:
            next = f'<li><a href="?{self.getquery_dict(self.total_page_count)}" aria-label="下一页"><span aria-hidden="true">下一页</span></a></li>'
        else:
            next = f'<li><a href="?{self.getquery_dict(self.page + 1)}" aria-label="下一页"><span aria-hidden="true">下一页</span></a></li>'
        page_str_list.append(next)
        # 尾页
        last_page = f'<li><a href="?{self.getquery_dict(self.total_page_count)}" aria-label="尾页"><span aria-hidden="true">尾页</span></a></li>'
        page_str_list.append(last_page)
        # 页码跳转
        search_str = '''
        <div style="float: right ; width: 200px">
            <form method="get">
                <div class="input-group">
                    <input name="page" type="text" class="form-control" placeholder="页码">
                    <span class="input-group-btn">
        <button class="btn btn-default" type="submit">跳转</button>
            </span>
                </div>
            </form>
        </div>
        '''
        page_str_list.append(search_str)
        page_string = mark_safe(''.join(page_str_list))
        return page_string
