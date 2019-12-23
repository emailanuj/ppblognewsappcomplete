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
    filtered_data=News.objects.filter(title='Test News 2')
    context={
        "data":news_list,
        "filtered_data":filtered_data
    }
    return render(request,'news.html',context)