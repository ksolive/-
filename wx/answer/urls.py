from django.urls import path
from . import views
urlpatterns = [
    path('commitAnswer/', views.commitAnswer, name='commitAnswer'),
    path('getAnswerList/',views.getAnswerList,name='getAnswerList'),
    path('getAnswer/',views.getAnswer,name="getAnswer"),
    path('deleteAnswer/',views.deleteAnswer,name='deleteAnswer'),
    path('addHelpful/',views.addHelpful,name='addHelpful')

]