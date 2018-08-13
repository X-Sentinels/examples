#!/usr/bin/python
#coding=utf-8

import commands
import time
import copy
import json
import requests
from multiprocessing.dummy import Pool as ThreadPool

def add_data(metric,value,conterType,tags):
    data = {"endpoint":endpoint,"metric":metric,"timestamp":ts,"step":step,"value":value,"counterType":conterType,"tags":tags}
    payload.append(copy.copy(data))

def curl(url):
    cmd = "curl -o /dev/null -s -w %{http_code}:%{http_connect}:%{time_namelookup}:%{time_redirect}:%{time_pretransfer}:%{time_connect}:%{time_starttransfer}:%{time_total}:%{speed_download} " + url
    status, output = commands.getstatusoutput(cmd)
    if status != 0:
        return False, "Call Curl Error"
    return True, output.split(":")

def add_payload(url):
    tag = "url=%s" % (url,)
    metrics = ["curl.http_code","curl.http_connect","curl.time_namelookup","curl.time_redirect","curl.time_pretransfer","curl.time_connect","curl.time_starttransfer","curl.time_total","curl.speed_download"]
    success, result = curl(url)
    if success == False:
        add_data("curl.success", 0, "GAUGE", tag)
    else:
        add_data("curl.success", 1, "GAUGE", tag)
        for index, metric in enumerate(metrics):
            add_data(metric, float(result[index]), "GAUGE", tag)

if __name__ == '__main__':
    push_url = "http://127.0.0.1:6060/api/push"
    endpoint = "ubuntu-pi"
    processes = 8
    step = 60
    urllist = ["http://www.ecnu.edu.cn","https://www.baidu.com","http://www.163.com","http://bbs.ngacn.cc","https://www.google.com.hk","https://cannotfound.com"]

    ts = int(time.time())
    payload = []

    pool = ThreadPool(processes)
    for url in urllist:
        pool.apply_async(add_payload, args=(url,))
    pool.close()
    pool.join()

    #print json.dumps(payload,indent=4)
    r = requests.post(push_url, data=json.dumps(payload))
