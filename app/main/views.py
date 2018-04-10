#-*- coding:utf-8 -*-
from flask import render_template, abort, request,jsonify, redirect,url_for,flash, current_app, send_from_directory
from . import main
from sqlalchemy import desc
from .. import db
from flask_login import login_user, logout_user, login_required
from ..models import User,ApiTest
import os,json, time
from ..email import send_email
from app import celery
import json as simplejson
import sys,requests

reload(sys)
sys.setdefaultencoding("utf-8")
IGNORED_FILES = set(['.gitignore'])

@main.route('/')
def index():
	return render_template('index.html')

@main.route('/data')
def data():
    ss = ApiTest.query.all()
    data = {"code":1,"msg":"success"}
    data["data"] = []

    for i in ss:
    	name =  i.to_json()["name"]
    	ctime =  int(time.mktime(time.strptime(str(i.to_json()['create_time']), "%Y-%m-%d %H:%M:%S")))
        data['data'].append([ctime, name])
    print data
    return json.dumps(data)
    # for i in cur.fetchall():
    #     arr.append([i[1]*1000,i[0]])
    # return json.dumps(arr)
    	
    
    #return  "data"

