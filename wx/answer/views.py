
from django.shortcuts import HttpResponse
from . import models
import json
import pymysql

# Create your views here.
def commitAnswer(request):
    print(request.POST.get('writerID'))
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
    sql = 'insert into answer_review(reviewText,writerID_id,questionID_id) values(%s,%s,%s)'
    rows = cursor.execute(sql,(request.POST.get("review"),request.POST.get("writerID"),request.POST.get("articleID")))
    conn.commit()

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()
    return HttpResponse(1)

def getAnswerList(request):
    id = request.POST.get("id")
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
    rows = cursor.execute('select * from answer_review where questionID_id=%s', id)
    answers=cursor.fetchall()
    user_id=1
    help=0


    answerList=[]
    for answer in answers:
        answeritem={}
        answeritem['answerID']=answer['id']
        answeritem['text']=answer['reviewText']
        answeritem['created']=str(answer['created'])
        answeritem['helpfulVote'] = answer['helpfulVote']
        answeritem['userid'] = answer['writerID_id']
        review_id = answer['id']
        rows1 = cursor.execute('select * from answer_review_users_like where user_id=%s and review_id=%s', (user_id,review_id))
        res=cursor.fetchone()
        print(res)
        if res==None:
            answeritem['isHelpful']=0
        else:
            answeritem['isHelpful'] = 1

        answerList.append(answeritem)

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()
    return HttpResponse(json.dumps(answerList))

def addHelpful(request):
    id=request.POST.get("id")
    isHelpful=int(request.POST.get("isHelpful"))
    userid=request.POST.get("userid")
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='ravvi3138',
        db='finaltest',
        charset='utf8'
    )

    # 获取游标

    review = models.Review.objects.get(id=id)
    print(isHelpful)
    if isHelpful == 0:
        print("addHelpful")
        cursor = conn.cursor()
        sql='update answer_review set helpfulVote=helpfulVote+1 where id=%s'
        rows = cursor.execute(sql,id)
        sql1='insert into answer_review_users_like(review_id,user_id) values(%s,%s)'
        rows1 = cursor.execute(sql1, (id,userid))
        conn.commit()
        cursor.close()
        conn.close()
    else:
        print("deleteHelpful")
        cursor = conn.cursor()
        sql = 'update answer_review set helpfulVote=helpfulVote-1 where id=%s'
        rows = cursor.execute(sql, id)
        sql1 = 'delete from answer_review_users_like where review_id=%s and user_id=%s'
        rows1 = cursor.execute(sql1, (id, userid))
        conn.commit()
        cursor.close()
        conn.close()
    return  HttpResponse(review.helpfulVote)

def deleteAnswer(request):
    id = request.POST.get("id")
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
    sql = 'delete from answer_review where id=%s'
    rows = cursor.execute(sql, id)
    conn.commit()

    # 关闭游标
    cursor.close()

    # 关闭连接
    conn.close()

    review = models.Review.objects.get(id=id)
    review.delete()
    return HttpResponse("deleted")

def getAnswer(request):
    id = request.POST.get("id")
    print(id)
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
    rows = cursor.execute('select * from answer_review where id=%s', id)
    answer = cursor.fetchone()
    cursor.close()

    # 关闭连接
    conn.close()
    print(answer)
    return HttpResponse(answer['reviewText'])