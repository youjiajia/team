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
    return render_to_response('index.html')

#畅言论坛
def bbs(req):
    response=render_to_response('index.html')
    if req.COOKIES.get('userid','')=='':
        access_token=getToken(sCorpSecret)
        code=req.GET.get('code')
        req = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token='+access_token+'&code='+code)
        response = urllib2.urlopen(req)
        the_page = response.read()
        jsonreturn=json.loads(the_page)
        if jsonreturn.has_key('UserId')
            response.set_cookie('userid',jsonreturn['UserId'])
    return response


#备忘录
class MemoTemplateView(TemplateView):
    template_name = 'memo/memor.html'
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated():
            return super(ForumIndexListView, self).dispatch(request, *args, **kwargs)
        else:
            return HttpResponseRedirect("/normal/login/")

    def get_context_data(self, **kwargs):
        context = super(ForumIndexListView, self).get_context_data(**kwargs)
        user = self.request.user
        setattr(user,"focusnum",user.userforum.userfocus.count())
        setattr(user,"fans",user.befocus_user.count())
        setattr(user,"signin",'true' if user.userforum.lastsigned_time == date.today() else 'false')
        context['user'] = user
        context['weekday'] = date.weekday(date.today())+1
        context['modules'] = ForumModule.objects.all()
        hottitles=ForumTitle.objects.order_by('-replynum')[:4]
        newtitles = ForumTitle.objects.order_by(
            "-title_createtime")[:7]
        for hottitle in hottitles:
            recentlyusers=hottitle.title_reply.order_by("reply_createtime")
            if recentlyusers.count()>0:
                setattr(hottitle,"replycontent",recentlyusers[0].replycontent)
            else:
                setattr(hottitle,"replycontent","0")
        context['hottitles']=hottitles
        for newtitle in newtitles:
            recentlyusers=newtitle.title_reply.order_by("-reply_createtime")
            if recentlyusers.count()>0:
                setattr(newtitle,"recentlyuser",recentlyusers[0].replyuser.username)
            else:
                setattr(newtitle,"recentlyuser","0")
        context['newtitles']=newtitles
        return context