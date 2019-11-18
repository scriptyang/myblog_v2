#conding: utf-8
from .models import Service_data

conf = {
    #name 和 remark 不需要进行匹配
    "data_structure":{
        "name": "vpn账号",
        "sn_num": "sn号码",
        "ssl": "sslip",
        "ppp": 'xl2ip',
        "remark": "备注"
    },
    "user_structure":{
        "id": "id",
        "username": "用户",
        "email": "邮箱",
        "groups": '用户组',
    },
    "service_num": Service_data.objects.all().count(),
}

