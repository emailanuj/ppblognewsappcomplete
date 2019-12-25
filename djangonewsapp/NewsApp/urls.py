from django.urls import path,include
from .views import NewsList,Home,About,Contact,Register,addUser,ModelForm,addModalForm
urlpatterns = [
    path('news/',NewsList,name='news'),
    path('home/',Home,name='home'),
    path('contact/',Contact,name='contact'),
    path('about/',About,name='about'),
    path('register/',Register,name='register'),
    path('addUser/',addUser,name='addUser'),
    path('modelform/',ModelForm,name='modelform'),
    path('addModalForm/',addModalForm,name='addModalForm')
]