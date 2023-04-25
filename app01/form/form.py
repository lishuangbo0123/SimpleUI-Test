from app01 import models
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from app01.utils.BootStrapModel import BootStrapModelForm

class NumEditModelForm(BootStrapModelForm):
    mobile = forms.CharField(disabled=True,label='手机号')
    class Meta:
        model = models.PrettyNum
        fields = ['mobile','price','level','status']
        # fields = '__all__'
        # exclude = ['mobile']

        # 验证 方式2

    def clean_mobile(self):
        # 当前编辑的那一行的ID
        # self.instance.pk
        txt_mobile = self.cleaned_data['mobile']
        exists = models.PrettyNum.objects.exclude(id = self.instance.pk).filter(mobile=txt_mobile).exists()
        if len(txt_mobile) != 11:
            raise ValidationError('格式错误')
        # 验证不通过
        elif exists:
            raise ValidationError('手机号已存在')

        return txt_mobile