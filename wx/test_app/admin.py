from django.contrib import admin
from .models import Article,MyUser,Volunteers,Experts
# Register your models here.
admin.site.register(Article)
admin.site.register(Volunteers)
admin.site.register(MyUser)
admin.site.register(Experts)
