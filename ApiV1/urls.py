from django.urls import path
from .views import *

urlpatterns = [
    # 用户信息
    path('user_list/', UserInfo.as_view(),name='user_info'),
    # 服务信息
    path('Service_info/', ServiceInfo.as_view(), name='service_info'),
    # 登录认证
    path('LoginAuth/', LoginAuth.as_view(), name='login'),
]