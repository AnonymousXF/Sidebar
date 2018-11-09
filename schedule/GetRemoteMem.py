import psutil
import urllib3
import json
from time import sleep


while True:
    meminfo = psutil.virtual_memory()
    cpuinfo = psutil.cpu_percent()
    mem_data = {}
    cpu_data = {}
    mem_data['total'] = meminfo.total
    mem_data['used'] = meminfo.used
    mem_data['free'] = meminfo.free
    mem_data['percent'] = meminfo.percent
    cpu_data['percent'] = cpuinfo

    http = urllib3.PoolManager()
    r = http.request('POST',
                     'http://127.0.0.1:5000/api/upload_meminfo',
                     body=json.dumps(mem_data).encode(),
                     headers={'Content-Type':'application/json'})
    print(r.data.decode('unicode_escape'))
    r = http.request('POST',
                     'http://127.0.0.1:5000/api/upload_cpuinfo',
                     body=json.dumps(cpu_data).encode(),
                     headers={'Content-Type':'application/json'})
    print(r.data.decode('unicode_escape'))
    sleep(20)

