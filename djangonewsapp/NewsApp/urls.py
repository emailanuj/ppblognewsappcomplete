from django.urls import path,include
from .views import NewsList,Home,About,Contact
urlpatterns = [
    path('news/',NewsList,name='news'),
    path('home/',Home,name='home'),
    path('contact/',Contact,name='contact'),
    path('about/',About,name='about')
]