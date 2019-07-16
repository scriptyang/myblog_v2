from django.db import models


class Service_data(models.Model):
    '''
    需要在conf 文件中进行列匹配
    '''
    name = models.CharField(max_length=20,primary_key=True)
    sn_num = models.CharField(max_length=255,default='')
    ssl = models.CharField(max_length=50,default='')
    remark = models.CharField(max_length=255,default='')
    ppp = models.CharField(max_length=50,default='')

class Settings_cmdb(models.Model):
    image = models.CharField(max_length=50)
    site_name = models.CharField(max_length=50,default='管理平台')
    user_image = models.CharField(max_length=50,default='/static/picture/user.png')

class Content(models.Model):
    file_name = models.CharField(max_length=100)
    file_content = models.TextField()
    file_remark = models.CharField(max_length=200,default='')

# Create your models here.
