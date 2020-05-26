from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class ArticlePost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 标题 models.CharField 为字符串字段，用于保存较短的字符串，如标题
    title = models.CharField(max_length=100)

    # 正文 TextField 保存大量文本
    body = models.TextField()

    # ImgaeField() 配合pillow 图像处理 upload_to到指定目录（年月日）
    picture = models.ImageField(upload_to='picture/%Y%m%d/', blank=True)

    # 创建时间 参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)

    # 更新时间 参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)

    privacy=models.IntegerField(default=0)

    class Meta:
            # ordering 指定模型返回的数据的排列顺序
            # '-created' 表明数据应该以倒序排列
            ordering = ('-created',)

        # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容
    def __str__(self):
            # return self.title 将文章标题返回
            return self.title


