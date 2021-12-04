from django.urls import path,include
from . import views
from django.http import HttpResponse
urlpatterns = [

    path('',views.home_page,name='home_page'),
    path('article/',views.show_article, name='article'),
    path('admin_profile/',views.admin_profile,name='admin_profile'),
    
]
