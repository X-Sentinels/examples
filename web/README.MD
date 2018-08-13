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