#-*- coding:utf-8 -*-
from flask import render_template, abort, request,jsonify, redirect,url_for,flash, current_app, send_from_directory
from . import main
from sqlalchemy import desc
from .. import db
from flask_login import login_user, logout_user, login_required
from ..models import User
import os,json
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

