#coding: utf-8

from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_login,name='login'),
    path('dashboard/',views.index,name='dashboard'),
    path('logout/',views.user_logout,name='logout'),
    path('settings/',views.settings),
    path('set_passwd/',views.set_passwd),
    path('user_list/',views.user_html),
    path('info_temp/',views.info_temp),
    path('task_temp/',views.task_temp),
    path('txt_list/',views.txt_html),
    path('file_view/<file_id>/',views.file_html),
    path('file_edit/<file_id>/',views.file_html),
    path('file_create/',views.txt_html),
]