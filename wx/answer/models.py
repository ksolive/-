from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Review(models.Model):
    reviewText = models.TextField(default="")
    questionID=models.ForeignKey('article.ArticlePost',related_name='reviews',on_delete=models.CASCADE)
    writerID=models.ForeignKey(User,related_name='write_review',on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='picture/%Y%m%d/', blank=True)
    # 创建时间 参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    created = models.DateTimeField(default=timezone.now)
    # 更新时间 参数 auto_now=True 指定每次数据更新时自动写入当前时间
    updated = models.DateTimeField(auto_now=True)
    id=models.BigAutoField(primary_key=True)
    helpfulVote = models.IntegerField(default=0)
    users_like = models.ManyToManyField(User, related_name="articlesLike", blank=True)
    class Meta:
        # ordering 指定模型返回的数据的排列顺序
        # '-created' 表明数据应该以倒序排列
        ordering = ('-helpfulVote', "-created",)