from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from . import models
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from login import views as login_views
import pymysql
import json
# Create your views here.
def index(request):
    return render(request,'test_app/index.html')

from django.contrib import auth

def login(request):
    
    username = request.POST.get('user', '')
    password = request.POST.get('psd', '')
    
    sql = 'select id,password from auther_user where name = "'+str(username)+'"'

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
    rows = cursor.execute(sql)
    artis=cursor.fetchall()

    if artis == ():
        cursor.close()
        conn.close()
        return HttpResponse(-2)
    else:
        if artis[0]['password'] == password:
            cursor.close()
            conn.close()
            return HttpResponse(artis[0]['id'])
        else:
            return HttpResponse(-1)
    '''
    try:
        user = models.MyUser.objects.get(username=username)
    except:
        return HttpResponse(-2)
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
    # Correct password, and the user is marked "active"
        auth.login(request, user)
    # Redirect to a success page.
        return HttpResponse(user.id)
    else:
    # Show an error page
        return HttpResponse(-1)
    '''
        

def signup(request):
    username = request.POST.get('user', '')
    password = request.POST.get('psd', '')
    
    sql = 'INSERT INTO auther_user (`name`, `password`) VALUES ('+'"'+str(username)+'"'+','+'"'+str(password)+'"'+');'
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='ravvi3138',
        db='finaltest',
        charset='utf8'
    )

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    sql = 'select id,password from auther_user where name = "'+str(username)+'"'
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    rows = cursor.execute(sql)
    artis=cursor.fetchall()

    '''
    user=models.MyUser.objects.create_user(username=username,password=password)
    user.save()
    '''
    cursor.close()
    conn.close()
    return HttpResponse(artis[0]['id'])
    


def userinfo(request):
    username = request.POST.get('user', '')

    sql = 'select * from auther_user where name = "'+str(username)+'"'
    print(sql)
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='ravvi3138',
        db='finaltest',
        charset='utf8'
    )

    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(sql)

    artis=cursor.fetchall()[0]

    cursor.close()
    conn.close()

    return HttpResponse(json.dumps(artis))

def userchange(request):
    userinfo = request.POST.get('userinfo','')
    id = request.POST.get('user','')

    sql = 'update auther_user set name=%s,sex=%s,job=%s,age=%s,like=%s where id=%s'
    print(sql)
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='ravvi3138',
        db='finaltest',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    rows = cursor.execute(sql, (userinfo['name'], userinfo['sex'], userinfo['job'],userinfo['age'], userinfo['like'],id ))
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return HttpResponse("编辑完成")

def userpowerup(request):
    id = request.POST.get('user','')

    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='ravvi3138',
        db='finaltest',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    sql = 'select power from auther_user where id=%s'
    rows = cursor.execute(sql,(id))
    power=int(cursor.fetchall()[0]['power'])

    sql = 'update auther_user set power%s where id=%s'
    rows = cursor.execute(sql,(str(power+1),id))
    conn.commit()

    cursor.close()
    conn.close()
    return HttpResponse('power up complated')
