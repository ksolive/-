from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
from article.models import ArticlePost
from django.contrib.auth.models import User
import json
# Create your views here.
def commitAnswer(request):
    review = request.POST.get("review")
    articleID = request.POST.get("articleID")
    writerID = request.POST.get("writerID")
    #testUser=User(id=1)
    #testUser.save()
    #testQuestion=ArticlePost(id=1)
    #testQuestion.author=testUser
    #testQuestion.save()

    thisreview = models.Review(reviewText=review,picture=request.POST.get("picture"))
    thisreview.writerID=User.objects.get(id=writerID)
    thisreview.questionID=ArticlePost.objects.get(id=articleID)
    thisreview.save()
    return HttpResponse(thisreview.id)

def getAnswerList(request):
    id=request.POST.get("id")
    userid=request.POST.get("userid")
    article=ArticlePost.objects.get(id=id)
    answers=article.reviews.all()
    answerList=[]
    try:
        user=User.objects.get(id=userid)
    except:
        print("没有登陆")
        user= 0
    for answer in answers:
        answeritem={}
        answeritem['answerID']=answer.id
        answeritem['text']=answer.reviewText
        answeritem['created']=answer.created.strftime('%Y-%m-%d')
        answeritem['helpfulVote'] = answer.helpfulVote
        answeritem['userid'] = answer.writerID.id

        print(answer.users_like.all())
        if user in answer.users_like.all():
            answeritem['isHelpful'] = 1
        else:
            answeritem['isHelpful'] = 0
        answerList.append(answeritem)
    return HttpResponse(json.dumps(answerList))

def addHelpful(request):
    id=request.POST.get("id")
    isHelpful=int(request.POST.get("isHelpful"))
    userid=request.POST.get("userid")
    review = models.Review.objects.get(id=id)
    print(isHelpful)
    if isHelpful == 0:
        print("addHelpful")
        review.helpfulVote=review.helpfulVote+1
        review.users_like.add(User.objects.get(id=userid))
        review.save()
    else:
        print("deleteHelpful")
        review.helpfulVote = review.helpfulVote - 1
        review.users_like.remove(User.objects.get(id=userid))
        review.save()
    return  HttpResponse(review.helpfulVote)

def deleteAnswer(request):
    id= request.POST.get("id")
    review = models.Review.objects.get(id=id)
    review.delete()
    return HttpResponse("deleted")

def getAnswer(request):
    id = request.POST.get("id")
    review=models.Review.objects.get(id=id)
    reviewText=review.reviewText
    print(reviewText)
    return HttpResponse(reviewText)