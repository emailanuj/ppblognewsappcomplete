from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import News,RegisterUser
from .forms import RegisterUserForm
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


def Register(request):
    context={
        "form":RegisterUserForm
    }
    return render(request,'register.html',context)

def addUser(request):
    form=RegisterUserForm(request.POST)

    if form.is_valid():
        registerUser=RegisterUser(username=form.cleaned_data['username'],
        password=form.cleaned_data['password'],
        email=form.cleaned_data['email'],
        phone=form.cleaned_data['phone'])
        registerUser.save()
    return redirect('home')