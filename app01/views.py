from django.shortcuts import render,HttpResponse
from .models import UserInfo,ClassList
from django.forms import ModelForm


class UserModelForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'


class ClassListModelForm(ModelForm):
    class Meta:
        model = ClassList
        fields = '__all__'


def test(request):
    obj = UserInfo.objects.create(usertype=1,user='Parker',pwd=123)
    for i in obj._meta.related_objects:
        print(i.field.model._meta.model_name,i.related_name,i.field_name,i.limit_choices_to)

    return HttpResponse('.....')




def index(request):
    form = ClassListModelForm()

    return render(request,'index.html',{'form':form})