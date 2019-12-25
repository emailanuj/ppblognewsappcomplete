from django.contrib import admin
from .models import News,SportsNews,RegisterUser
# Register your models here.
admin.site.register(News)
admin.site.register(SportsNews)
admin.site.register(RegisterUser)