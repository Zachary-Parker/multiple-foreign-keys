from django.db import models


class UserInfo(models.Model):

    user = models.CharField(max_length=32)
    pwd = models.CharField(max_length=32)
    userType_choices = (
        (1,'讲师'),
        (2,'班主任')
    )
    usertype = models.IntegerField(choices=userType_choices)


class ClassList(models.Model):
    name = models.CharField(max_length=32)
    teacher = models.ForeignKey(to=UserInfo,to_field='id',limit_choices_to={'usertype':1},related_name='TcLs')
    headmaster = models.ForeignKey(to=UserInfo,to_field='id',limit_choices_to={'usertype':2})


