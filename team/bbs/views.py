# -*- coding: utf-8 -*-  
#coding=utf-8 
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import json,urllib,urllib2
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
from django.views.generic import ListView, TemplateView
import xml.etree.cElementTree as ET
from public.views import getToken
from teamdb.models import *
# Create your views here.
basePath=os.path.dirname(os.path.dirname(__file__))
logPath=os.path.join(basePath,"log/indexviewError.txt")
informationStateXml=os.path.join(basePath,"webStatic/xml/weiConfig.xml")
tree = ET.ElementTree(file=informationStateXml)
sToken = tree.find("sToken").text
sEncodingAESKey = tree.find("sEncodingAESKey").text
sCorpID = tree.find("sCorpID").text
sCorpSecret = tree.find("sCorpSecret").text

#平台管理
def people(req):
    return render_to_response('index.html')
#项目管理
def project(req):
    return HttpResponse(req.COOKIES.get('userid'))

#畅言论坛
def bbs(req):
    response=render_to_response('index.html')
    if req.COOKIES.get('userid','')=='':
        access_token=getToken(sCorpSecret)
        code=req.GET.get('code')
        urlreq = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token='+access_token+'&code='+code)
        urlresponse = urllib2.urlopen(urlreq)
        the_page = urlresponse.read()
        jsonreturn=json.loads(the_page)
        if jsonreturn.has_key('UserId'):
            response.set_cookie('userid',jsonreturn['UserId'])
    return response


#备忘录
class MemoTemplateView(TemplateView):
    template_name = 'memo/memor.html'
    def dispatch(self, request, *args, **kwargs):
        response=super(MemoTemplateView, self).dispatch(request, *args, **kwargs)
        if request.COOKIES.get('userid','')=='':
            access_token=getToken(sCorpSecret)
            code=request.GET.get('code')
            urlreq = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token='+access_token+'&code='+code)
            urlresponse = urllib2.urlopen(urlreq)
            the_page = urlresponse.read()
            jsonreturn=json.loads(the_page)
            if jsonreturn.has_key('UserId'):
                if T_Member.objects.filter(UserID=jsonreturn['UserId'],IsUsed=True).count()==0:
                    T_Member.objects.create(UserID=jsonreturn['UserId'],IsUsed=True)
                self.response_class.set_cookie('userid',jsonreturn['UserId'])
        return response

    def get_context_data(self, **kwargs):
        context = super(MemoTemplateView, self).get_context_data(**kwargs)
        context['memo']=T_Memo.objects.all()#filter(MemberId=T_Member.objects.get(UserID=self.request.COOKIES.get('userid'))).order_by('-CreateTime')
        return context