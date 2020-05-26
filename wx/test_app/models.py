from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    author=models.ForeignKey(User,related_name='write_art',on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    body=models.TextField()
    create_time=models.DateTimeField(default=timezone.now)
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class MyUser(User):
    power = models.IntegerField(default=0)
    #headicon = models.FileField(upload_to='img/')
    #iconid = 
    class Meta:
        verbose_name = u"普通用户"
        verbose_name_plural = u"普通用户"


class Experts(MyUser):
    patients = models.ManyToManyField(MyUser,related_name='my_experts')

    class Meta:
        verbose_name = u"专家"
        verbose_name_plural = u"专家"


class Volunteers(MyUser):
    patients = models.ManyToManyField(MyUser,related_name='my_volunteers')

    class Meta:
        verbose_name = u"志愿者"
        verbose_name_plural = u"志愿者"



