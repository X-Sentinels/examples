#coding=utf-8 
from flask import request, jsonify, Response, render_template
import jinja2
from functools import wraps
from app import app

def require_appkey(view_function):
    @wraps(view_function)
    # the new, post-decoration function. Note *args and **kwargs here.
    def decorated_function(*args, **kwargs):
        if request.headers.get('X-API-KEY') and request.headers.get('X-API-KEY') == app.config["KEY"]:
            return view_function(*args, **kwargs)
        else:
            result = {"success":False,"msg":"missing X-API-KEY or KEY is Wrong"}
            return jsonify(result),401
    return decorated_function

@app.route('/api/v1/version', methods=['GET'])
@require_appkey
def version():
    return jsonify({"success":True, "version":app.config["VERSION"]}), 200

@app.route('/api/v1/hello', methods=['GET'])
def hello():
    return jsonify({"success":True, "msg":"hello world"}), 200

@app.route('/hello', methods=['GET'])
def hello_view():
    resp = Response(render_template('hello.html', version = app.config["VERSION"]))
    return resp, 200
