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
    cookieuserid=''
    def getuserid(self,request):
        access_token=getToken(sCorpSecret)
        code=request.GET.get('code')
        urlreq = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token='+access_token+'&code='+code)
        urlresponse = urllib2.urlopen(urlreq)
        the_page = urlresponse.read()
        jsonreturn=json.loads(the_page)
        if jsonreturn.has_key('UserId'):
            cookieuserid=jsonreturn['UserId']
    def dispatch(self, request, *args, **kwargs):
        response=super(MemoTemplateView, self).dispatch(request, *args, **kwargs)
        if request.COOKIES.get('userid','')=='':
            print cookieuserid
            if cookieuserid!='':
                if T_Member.objects.filter(UserID=cookieuserid,IsUsed=True).count()==0:
                    T_Member.objects.create(UserID=cookieuserid,IsUsed=True)
                response.set_cookie('userid',cookieuserid)
        return response
    def get_context_data(self, **kwargs):
        context = super(MemoTemplateView, self).get_context_data(**kwargs)
        if self.request.COOKIES.get('userid','')=='':
            getuserid(self.request)
            if cookieuserid!='':
                if T_Member.objects.filter(UserID=cookieuserid,IsUsed=True).count()==0:
                    T_Member.objects.create(UserID=cookieuserid,IsUsed=True)
                context['memo']=T_Memo.objects.filter(MemberId=T_Member.objects.get(UserID=cookieuserid)).order_by('-CreateTime')
                return context
        else:
            context['memo']=T_Memo.objects.filter(MemberId=T_Member.objects.get(UserID=self.request.COOKIES.get('userid'))).order_by('-CreateTime')
            return context
def addmemo(req):
    if req.method=='GET':
        return render_to_response('memo/addmemor.html')
    elif req.method=='POST':
        if req.COOKIES.get('userid','')!='':
            T_Memo.objects.create(MemberId=req.COOKIES.get('userid'),MimoContent=req.POST.get('content'))
            return HttpResponse('1')
        else:
            return HttpResponse('0')
def memodetail(req):
    if req.method=='GET':
        if req.GET.get('id','')!='':
            memo=T_Memo.objects.get(id=req.GET.get('id'))
            return render_to_response('memo/memordetail.html',{'memo':memo})
    elif req.method=='POST':
        if req.COOKIES.get('userid','')!='' & req.POST.get('content','')!='':
            T_Memo.objects.get(id=req.POST.get('id')).update(MimoContent=req.POST.get('content'))
            return HttpResponse('1')
        else:
            return HttpResponse('0')
def deletememo(req):
    if req.GET.get('id','')!='':
        T_Memo.objects.get(id=req.GET.get('id')).delete()
        return HttpResponse('1')
    return HttpResponse('0')