from django import forms
class BootStrapModelForm(forms.ModelForm):


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        #循环找到所有的插件，添加了class="form-control"
        for name,field in self.fields.items():
            if field.widget.attrs:
                field.widget.attrs['class'] = "form-control"
                field.widget.attrs['placeholder'] = field.label
            else:
                field.widget.attrs = {"class":"form-control",
                                      "placeholder":field.label}