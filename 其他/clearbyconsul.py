# !/usr/bin/python
# encoding:utf-8
import requests
import json

gatewayurl="http://192.168.0.105:8500/"
'''depend on consul ,do not depend on gateway'''
def QueryServices():
    api_GetAllServices=gatewayurl+"v1/internal/ui/services"
    r=requests.get(api_GetAllServices)
    services=json.loads(r.text)
    for srv in services:
        if(srv["ChecksCritical"]>0):
            r=requests.get(gatewayurl+"v1/health/service/%s"%srv["Name"])
            ClearServices(json.loads(r.text))
    
def ClearServices(srvs):
    for srv in srvs:
        for check in srv["Checks"]:
            if(check["Status"]=="critical"):
                registerid=check["ServiceID"]
                api_deregister=gatewayurl+"v1/agent/service/deregister/%s"%registerid
                requests.put(api_deregister)

QueryServices()

