### falcon Example

falcon 相关的 API 的请求 example

#### 安装
##### 环境准备
```
# apt-get install python-pip
# pip install virtualenv
```
##### 虚拟环境准备
```
# git clone https://github.com/X-Sentinels/examples
# cd falcon
# virtualenv env
# ./env/bin/pip install -r requirement.txt 
```

#### 运行
```
# ./env/bin/python getData.py 
```

#### 应用
```
if __name__ == '__main__':
    api_addr = "http://127.0.0.1:8080/api/v1"
    # falcon 的 api 地址
    name = "username"
    # falcon 的用户名
    password = "password"
    # falcon 的密码

    end_time = int(time.time())
    start_time = end_time - 3600
    # 查询的时间范围

    d = {
         "step": 60,
         #数据的步长
         "start_time": start_time,
         #查询的起始时间
         "hostnames": [
                       "Master"
                      ],
         #查询的 endpoint 列表
         "end_time": end_time,
         #查询的结束时间
         "counters": [
                      "humidity/facility=raspberry",
                      "temperature/facility=raspberry"
                     ],
         #查询的 counter
         "consol_fun": "AVERAGE"
         #查询的取值(MAX, MIN, AVERAGE)
        }
    # 请求 body

    try:
        Apitoken = get_Apitoken(name, password, api_addr)
        #先获取 Apitoken
        res = get_History(Apitoken, d, api_addr)
        #再请求 history 接口获取历史数据
        print res
    except Exception as e:
        print e
```