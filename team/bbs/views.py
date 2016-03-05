# -*- coding: utf-8 -*-  
#coding=utf-8 
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json
import StringIO
import os,base64
import time
import uuid
from datetime import datetime
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
basePath=os.path.dirname(os.path.dirname(__file__))
logPath=os.path.join(basePath,"log/indexviewError.txt")


#平台管理
@csrf_exempt
def people(req):
        return render_to_response('index.html')

#项目管理
@csrf_exempt
def project(req):
        return render_to_response('index.html')

#畅言论坛
@csrf_exempt
def bbs(req):
        return render_to_response('index.html')

#备忘录
@csrf_exempt
def memo(req):
        return render_to_response('index.html')