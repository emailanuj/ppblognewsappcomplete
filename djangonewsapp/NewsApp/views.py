from django.shortcuts import render
from django.shortcuts import HttpResponse
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

def News(request):
    return render(request,'news.html')