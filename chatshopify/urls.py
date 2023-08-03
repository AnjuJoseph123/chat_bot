from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('',views.welcome,name='welcome'),
    path('signup', views.Signup,name='Signup'),
    path('', views.Login,name='Login'),
    path('login', views.Login,name='Login'),
    path('index', views.index,name='index'),
    path('logout', views.LogoutPage,name='logout'),
    path('user-profile', views.userprofile,name='user-profile'),
    path('savechanges', views.savechanges,name='savechanges'),
    path('upload_dataset', views.upload_dataset,name='upload_dataset'),
    path('save_file', views.save_file,name='save_file'),
    path('app_chat_box', views.app_chat_box,name='app_chat_box'),
    path('question_answering', views.question_answering,name='question_answering'),
    
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)