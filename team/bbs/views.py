# -*- coding: utf-8 -*-
# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import json
import urllib
import urllib2
import StringIO
import os
import base64
import time
import uuid
from datetime import datetime
from django.db import transaction
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
import xml.etree.cElementTree as ET
from public.views import getToken, getDepartmentList
from teamdb.models import *
# Create your views here.
basePath = os.path.dirname(os.path.dirname(__file__))
logPath = os.path.join(basePath, "log/indexviewError.txt")
informationStateXml = os.path.join(basePath, "webStatic/xml/weiConfig.xml")
tree = ET.ElementTree(file=informationStateXml)
sToken = tree.find("sToken").text
sEncodingAESKey = tree.find("sEncodingAESKey").text
sCorpID = tree.find("sCorpID").text
sCorpSecret = tree.find("sCorpSecret").text

# 平台管理


def people(req):
    return render_to_response('index.html')


# 畅言论坛
def bbs(req):
    response = render_to_response('index.html')
    if req.COOKIES.get('userid', '') == '':
        access_token = getToken(sCorpSecret)
        code = req.GET.get('code')
        urlreq = urllib2.Request(
            'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token='+access_token+'&code='+code)
        urlresponse = urllib2.urlopen(urlreq)
        the_page = urlresponse.read()
        jsonreturn = json.loads(the_page)
        if jsonreturn.has_key('UserId'):
            response.set_cookie('userid', jsonreturn['UserId'])
    return response


# 备忘录
class MemoTemplateView(TemplateView):
    template_name = 'memo/memor.html'
    cookieuserid = ''

    def getuserid(self, request):
        access_token = getToken(sCorpSecret)
        code = request.GET.get('code')
        urlreq = urllib2.Request(
            'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token='+access_token+'&code='+code)
        urlresponse = urllib2.urlopen(urlreq)
        the_page = urlresponse.read()
        jsonreturn = json.loads(the_page)
        if jsonreturn.has_key('UserId'):
            self.cookieuserid = jsonreturn['UserId']

    def dispatch(self, request, *args, **kwargs):
        response = super(MemoTemplateView, self).dispatch(
            request, *args, **kwargs)
        if request.COOKIES.get('userid', '') == '':
            if self.cookieuserid != '':
                if T_Member.objects.filter(UserID=self.cookieuserid, IsUsed=True).count() == 0:
                    T_Member.objects.create(
                        UserID=self.cookieuserid, IsUsed=True)
                response.set_cookie('userid', self.cookieuserid)
        return response

    def get_context_data(self, **kwargs):
        context = super(MemoTemplateView, self).get_context_data(**kwargs)
        if self.request.COOKIES.get('userid', '') == '':
            self.getuserid(self.request)
            if self.cookieuserid != '':
                if T_Member.objects.filter(UserID=self.cookieuserid, IsUsed=True).count() == 0:
                    T_Member.objects.create(
                        UserID=self.cookieuserid, IsUsed=True)
                context['memo'] = T_Memo.objects.filter(
                    MemberId=T_Member.objects.get(UserID=self.cookieuserid)).order_by('-CreateTime')
                return context
        else:
            context['memo'] = T_Memo.objects.filter(MemberId=T_Member.objects.get(
                UserID=self.request.COOKIES.get('userid'))).order_by('-CreateTime')
            return context
# 添加备忘录


def addmemo(req):
    if req.method == 'GET':
        return render_to_response('memo/addmemor.html')
    elif req.method == 'POST':
        if req.COOKIES.get('userid', '') != '':
            T_Memo.objects.create(MemberId=T_Member.objects.get(
                UserID=req.COOKIES.get('userid')), MimoContent=req.POST.get('content'))
            return HttpResponse('1')
        else:
            return HttpResponse('0')
# 查看备忘录


def memodetail(req):
    if req.method == 'GET':
        if req.GET.get('id', '') != '':
            memo = T_Memo.objects.get(id=req.GET.get('id'))
            return render_to_response('memo/memordetail.html', {'memo': memo})
    elif req.method == 'POST':
        print type(req.POST.get('content', 'nothing'))
        if req.COOKIES.get('userid', '') != '':
            print req.POST.get('id')
            memo = T_Memo.objects.get(id=req.POST.get('id'))
            memo.MimoContent = req.POST.get('content')
            memo.save()
            return HttpResponse('1')
        else:
            return HttpResponse('0')
# 删除备忘录


def deletememo(req):
    if req.GET.get('id', '') != '':
        T_Memo.objects.get(id=req.GET.get('id')).delete()
        return HttpResponse('1')
    return HttpResponse('0')

# 项目管理


def project(req):
    response = render_to_response('project/promanage.html')
    if req.COOKIES.get('userid', '') == '':
        access_token = getToken(sCorpSecret)
        code = req.GET.get('code')
        urlreq = urllib2.Request(
            'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token='+access_token+'&code='+code)
        urlresponse = urllib2.urlopen(urlreq)
        the_page = urlresponse.read()
        jsonreturn = json.loads(the_page)
        if jsonreturn.has_key('UserId'):
            if T_Member.objects.filter(UserID=jsonreturn['UserId'], IsUsed=True).count() == 0:
                T_Member.objects.create(
                    UserID=jsonreturn['UserId'], IsUsed=True)
            response.set_cookie('userid', jsonreturn['UserId'])
    return response
# 项目列表


def projectindex(req):
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    if T_Admin.objects.filter(MemberId=member).count() != 0:
        list = []
        for admin in T_Admin.objects.filter(MemberId=member):
            list.append(admin.Department_ID)
        projects = T_Project.objects.filter(Department_ID__in=list)
        return render_to_response('project/projectlist.html', {"level": "admin", "projects": projects})
    else:
        projectmembers = T_ProjectMember.objects.filter(MemberId=member)
        list = []
        for pmber in projectmembers:
            list.append(pmber.ProjectId.id)
        projects = T_Project.objects.filter(id__in=list)
        return render_to_response('project/projectlist.html', {"level": "member", "projects": projects})
# 添加项目


def projectadd(req):
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    if req.method == 'GET':
        admins = T_Admin.objects.filter(MemberId=member)
        dejsons = getDepartmentList()
        for admin in admins:
            for dejson in dejsons:
                if admin.Department_ID == dejson['id']:
                    setattr(admin, 'Departmentname', dejson['name'])
        render_to_response('project/projectadd.html', {'admins': admins})
    else:
        with transaction.commit_on_success():
            pro = T_Project.objects.create(AdminId=T_Admin.objects.get(MemberId=member, Department_ID=int(req.POST.get('Department_ID', '1'))), Department_ID=int(req.POST.get('Department_ID', '1')), ProjectName=req.POST.get(
                'ProjectName'), ProjectStartTime=req.POST.get('ProjectStartTime'),
                ProjectEndTime=req.POST.get('ProjectStartTime'),
                ProjectDescribe=req.POST.get('ProjectStartTime'),
                ProjectStatus=req.POST.get('ProjectStatus'))
            members = req.POST.get('members').split(',')
            headers = req.POST.get('headers').split(',')
            for memberid in members:
                isheader = False
                if memberid in headers:
                    isheader = True
                T_ProjectMember.objects.create(ProjectId=pro, AdminId=T_Admin.objects.get(MemberId=member, Department_ID=int(
                    req.POST.get('Department_ID', '1'))), MemberId=T_Member.objects.get(UserID=memberid), isHead=isheader)
        return HttpResponse('success')
