### WEB Example

一个简单的 flask web 服务 example

#### 安装
##### 环境准备
```
# apt-get install python-pip
# pip install virtualenv
```
##### 虚拟环境准备
```
# git clone https://github.com/X-Sentinels/examples
# cd web
# virtualenv env
# ./env/bin/pip install -r requirement.txt 
# chmod +x control
```

#### 运行
启动
```
./control start
```
停止
```
./control stop
```

#### debug
先退出 gunicorn
```
./control stop
```
然后直接运行以 debug
```
./env/bin/python run.py
```

#### 示例
##### /hello
```
# curl http://127.0.0.1:1234/hello
<html>
    hellow world , version is 0.0.1
</html>
```
##### /api/v1/hello
```
# curl http://127.0.0.1:1234/api/v1/version
{"msg":"missing X-API-KEY or KEY is Wrong","success":false}
```
##### /api/v1/version
需要 X-API-KEY 授权
成功示例
```
# curl -H "X-API-Key: ffa868e21ebcd17cc561cabcc4c7c90f" http://127.0.0.1:1234/api/v1/version
{"success":true,"version":"0.0.1"}
```
失败示例
```
# curl http://127.0.0.1:1234/api/v1/version
{"msg":"missing X-API-KEY or KEY is Wrong","success":false}
```