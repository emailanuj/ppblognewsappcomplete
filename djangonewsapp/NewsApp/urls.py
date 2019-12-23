from django.urls import path,include
from .views import News,Home,About,Contact
urlpatterns = [
    path('news/',News,name='news'),
    path('home/',Home,name='home'),
    path('contact/',Contact,name='contact'),
    path('about/',About,name='about')
]