from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import News
# Create your views here.
def Home(request):
    context={
        'Name':'Anuj Kumar Dubey',
        'programming_languages':['PHP','Python','Java','C++','SQL']
    }
    return render(request,'home.html',context)

def About(request):
    return render(request,'about.html')

def Contact(request):
    return render(request,'contact.html')

def NewsList(request):
    news_list=News.objects.all()
    context={
        "data":news_list
    }
    return render(request,'news.html',context)