 
from django.contrib import admin
from django.urls import path
from user_auth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name = 'register'),
    path('', login, name='login'),
    path('home/', home, name='home'),


]
