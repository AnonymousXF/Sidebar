# -*- coding:utf-8 -*-
from flask import render_template, request, jsonify
import os
import csv
import json
from . import dashboard
from . import info
from .. import DBSession
from ..models import Host

@dashboard.route('/')
def dashboard_index():
    return render_template("dashboard.html")

@dashboard.route('/appendSingleHost', methods=['POST'])
def AppendSingleHost():
    raw_data = request.get_json()
    # print(raw_data)
    session = DBSession()
    try:
        if raw_data['hostpwd'] == raw_data['hostpwd_confirm']:
            host = Host(host_name=raw_data['hostname'],
                        host_ip=raw_data['hostip'],
                        user=raw_data['hostuser'],
                        pwd=raw_data['hostpwd'])
            session.add(host)
            session.commit()
            session.close()
            return info.alert_success("添加成功！")
        else:
            session.close()
            return info.alert_warning("前后两次输入密码不一致！")
    except Exception as e:
        print(e)
        session.close()
        return info.aler_danger("主机信息已存在，添加失败！")

@dashboard.route('/uploadapi', methods=['POST'])
def Upload():
    try:
        file = request.files['file']
        filename = file.filename
        if filename.endswith(".csv"):
            base = os.getcwd()
            path = os.path.join(base, 'temporary')
            file.save(os.path.join(path, filename))
            return '上传成功！'
        else:
            return "只支持csv格式的文件！"
    except Exception as e:
        return "上传失败！Error：" + e.__repr__()

@dashboard.route('/appendHosts', methods=['POST'])
def AppendHosts():
    raw_data = request.get_json()
    filename = raw_data['filename'].split('\\')[-1]
    base = os.path.abspath(".")
    path = base + "/temporary/"
    session = DBSession()
    try:
        csv_file = csv.reader(open(path + filename, 'r', encoding='utf-8'))
        for line in csv_file:
            host = Host(host_name=line[0],
                        host_ip=line[1],
                        user=line[2],
                        pwd=line[3])
            session.add(host)
        session.commit()
        session.close()
        return info.alert_success("添加成功！")
    except Exception as e:
        print(e)
        session.close()
        return info.aler_danger("添加失败！请检查主机信息文件！")

@dashboard.route('/queryhosts')
def QueryHosts():
    data = []
    session = DBSession()
    results = session.query(Host).all()
    for result in results:
        r = {}
        r['host_name'] = result.host_name
        r['host_ip'] = result.host_ip
        r['primarykey'] = [result.host_ip, result.user]
        data.append(r)
    session.close()
    return json.dumps(data)

@dashboard.route('/hostinfo')
def HostInfo():
    return render_template("host_template.html")
