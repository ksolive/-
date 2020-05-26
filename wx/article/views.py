from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ArticlePostForm
from django.contrib.auth.models import User
from .models import ArticlePost
import json
from django.utils import timezone
import datetime
import pymysql
def article_list(request):
    list1=[]
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='ravvi3138',
        db='finaltest',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    rows = cursor.execute('select * from article_post order by updated desc;')
    artis=cursor.fetchall()
    # print(artis)
    for arti in artis:
        if arti['privacy']==0:
            data1={}
            data1['id']=arti['id']
            data1['title']=arti['title']
            data1['body']=arti['body']
            list1.append(data1)
        else:
            continue
    # print(list1)
    cursor.close()
    conn.close()
    return HttpResponse(json.dumps(list1))
    #return render(request, 'article/list.html', context)
    #return render(request,{'context':context})

def article_Mylist(request):
    user = request.GET.get('user','')
    list1 = []
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='ravvi3138',
        db='finaltest',
        charset='utf8'
    )
    # 获取游标
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    print(user)
    rows = cursor.execute('select * from article_post where author_id=%s order by updated desc;',user)
    artis = cursor.fetchall()
    print(artis)
    for arti in artis:
        
        data1 = {}
        data1['id'] = arti['id']
        data1['title'] = arti['title']
        data1['body'] = arti['body']
        list1.append(data1)

    cursor.close()
    conn.close()
    return HttpResponse(json.dumps(list1))

def article_detail(request, id):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='ravvi3138',
        db='finaltest',
        charset='utf8'
    )

    # 获取游标
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    rows = cursor.execute('select * from article_post where id=%s',id)
    arti = cursor.fetchone()
    print(arti)
    list1 = []
    data1 = {}
    data1['id'] = arti['id']
    data1['title'] = arti['title']
    data1['body'] = arti['body']
    list1.append(data1)
    print(list1)
    cursor.close()
    conn.close()
    return HttpResponse(json.dumps(list1))
    #return render(request, 'article/detail.html', context)


def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        # 将提交的数据赋值到表单实例中
        article_post_form = ArticlePostForm(data=request.POST)
        #print(article_post_form)
        # print(request.user)
        value={}
        value['title']=request.POST['title']
        value['body'] = request.POST['body']
        value['privacy'] = request.POST['privacy']
        value['id'] = request.POST['user']
        value['updated']=str(datetime.datetime.now())
        value['created'] = str(datetime.datetime.now())

        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='ravvi3138',
            db='finaltest',
            charset='utf8'
        )

        # 获取游标
        cursor = conn.cursor()
        sql='insert into article_post(title,body,created,updated,author_id,privacy) values(%s,%s,%s,%s,%s,%s)'
        rows = cursor.execute(sql, (value['title'], value['body'], value['updated'], value['created'], value['id'], value['privacy']))
        conn.commit()

        # 关闭游标
        cursor.close()

        # 关闭连接
        conn.close()
        # 判断提交的数据是否满足模型的要求
    return HttpResponse(1)



def article_delete(request, id):
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='ravvi3138',
        db='finaltest',
        charset='utf8'
    )
    # 获取游标
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql='delete from article_post where id=%s'
    rows = cursor.execute(sql,id)
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return HttpResponse(1)


def article_update(request, id):
    if request.method == "POST":
        value = {}
        value['title'] = request.POST['title']
        value['body'] = request.POST['body']
        value['privacy'] = request.POST['privacy']
        value['updated'] = str(datetime.datetime.now())

        conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='ravvi3138',
            db='finaltest',
            charset='utf8'
        )

        # 获取游标
        cursor = conn.cursor()
        sql = 'update article_post set title=%s,body=%s,privacy=%s,updated=%s where id=%s'
        rows = cursor.execute(sql, (value['title'], value['body'], value['privacy'],value['updated'], id ))
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return HttpResponse("编辑完成")