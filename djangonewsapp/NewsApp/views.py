from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from .models import News,RegisterUser
from .forms import RegisterUserForm,RegisterModel
from django.contrib import messages

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
        messages.add_message=(request, messages.SUCCESS, "You have been rigistered successfully!")
    return redirect('register')

def ModelForm(request):
    context={
        'modelform':RegisterModel
    }
    return render(request,'model-form.html',context)

def addModalForm(request):
    myModalForm=RegisterModel(request.POST)
    if myModalForm.is_valid():
        myModalForm.save()
    return redirect('home')