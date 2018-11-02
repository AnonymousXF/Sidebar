# -*- coding:utf-8 -*-
from flask import render_template, request
from . import dashboard
from . import info
from .. import db
from ..models import Host

@dashboard.route('/')
def dashboard_index():
    return render_template("dashboard.html")

@dashboard.route('/appendSingleHost', methods=['POST'])
def appendSingleHost():
    raw_data = request.get_json()
    # print(raw_data)
    try:
        if raw_data['hostpwd'] == raw_data['hostpwd_confirm']:
            host = Host(host_name=raw_data['hostname'],
                        host_ip=raw_data['hostip'],
                        user=raw_data['hostuser'],
                        pwd=raw_data['hostpwd'])
            db.add(host)
            db.commit()
            return info.alert_success("添加成功！")
        else:
            return info.alert_warning("前后两次输入密码不一致！")
    except Exception as e:
        print(e)
        return info.aler_danger("主机信息已存在，添加失败！")
