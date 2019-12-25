from django.urls import path,include
from .views import NewsList,Home,About,Contact,Register,addUser
urlpatterns = [
    path('news/',NewsList,name='news'),
    path('home/',Home,name='home'),
    path('contact/',Contact,name='contact'),
    path('about/',About,name='about'),
    path('register/',Register,name='register'),
    path('addUser/',addUser,name='addUser')
]