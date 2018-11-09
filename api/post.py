from flask import request
from datetime import datetime
import json
from . import api
from ..models import MemInfo, CPUInfo
from .. import DBSession

@api.route('/upload_meminfo', methods=['POST'])
def upload_meminfo():
    raw_data = request.json
    #print(raw_data)
    meminfo = MemInfo(host='127.0.0.1',
                      mem_total=raw_data['total'],
                      mem_used=raw_data['used'],
                      mem_free=raw_data['free'],
                      percent=raw_data['percent'],
                      timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    session = DBSession()
    session.add(meminfo)
    session.commit()
    session.close()
    return 'OK'

@api.route('/upload_cpuinfo', methods=['POST'])
def upload_cpuinfo():
    raw_data = request.json
    #print(raw_data)
    cpuinfo = CPUInfo(host='127.0.0.1',
                      cpu_percent=raw_data['percent'],
                      timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    session = DBSession()
    session.add(cpuinfo)
    session.commit()
    session.close()
    return 'OK'

@api.route('/get_meminfo/<path:hostip>', methods=['GET'])
def get_meminfo(hostip):
    session = DBSession()
    res = session.query(MemInfo).order_by(MemInfo.timestamp.desc()).filter(MemInfo.host == hostip).limit(20)
    timestamp = [r.timestamp.strftime("%y-%m-%d %H:%M:%S") for r in res]
    percent = [r.percent for r in res]
    session.close()
    timestamp.reverse()
    percent.reverse()
    return json.dumps({'timestamp': timestamp, 'percent': percent})

@api.route('/get_cpuinfo/<path:hostip>', methods=['GET'])
def get_cpuinfo(hostip):
    session = DBSession()
    res = session.query(CPUInfo).order_by(CPUInfo.timestamp.desc()).filter(CPUInfo.host == hostip).limit(20)
    timestamp = [r.timestamp.strftime("%y-%m-%d %H:%M:%S") for r in res]
    percent = [r.cpu_percent for r in res]
    session.close()
    timestamp.reverse()
    percent.reverse()
    return json.dumps({'timestamp': timestamp, 'percent': percent})
