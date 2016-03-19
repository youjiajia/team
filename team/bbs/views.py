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

basePath = os.path.dirname(os.path.dirname(__file__))
logPath = os.path.join(basePath, "log/indexviewError.txt")
informationStateXml = os.path.join(basePath, "webStatic/xml/weiConfig.xml")
tree = ET.ElementTree(file=informationStateXml)
sToken = tree.find("sToken").text
sEncodingAESKey = tree.find("sEncodingAESKey").text
sCorpID = tree.find("sCorpID").text
sCorpSecret = tree.find("sCorpSecret").text


def people(req):
    # 平台管理
    return render_to_response('index.html')


def bbs(req):
    # 畅言论坛
    response = render_to_response('index.html')
    if req.COOKIES.get('userid', '') == '':
        access_token = getToken(sCorpSecret)
        code = req.GET.get('code')
        urlreq = urllib2.Request(
            'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token=' + access_token + '&code=' + code)
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
            'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token=' + access_token + '&code=' + code)
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


def addmemo(req):
    # 添加备忘录
    if req.method == 'GET':
        return render_to_response('memo/addmemor.html')
    elif req.method == 'POST':
        if req.COOKIES.get('userid', '') != '':
            T_Memo.objects.create(MemberId=T_Member.objects.get(
                UserID=req.COOKIES.get('userid')), MimoContent=req.POST.get('content'))
            return HttpResponse('1')
        else:
            return HttpResponse('0')


def memodetail(req):
    # 查看备忘录
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


def deletememo(req):
    # 删除备忘录
    if req.GET.get('id', '') != '':
        T_Memo.objects.get(id=req.GET.get('id')).delete()
        return HttpResponse('1')
    return HttpResponse('0')


def project(req):
    # 项目管理
    if req.COOKIES.get('userid', '') == '':
        access_token = getToken(sCorpSecret)
        code = req.GET.get('code')
        urlreq = urllib2.Request(
            'https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token=' + access_token + '&code=' + code)
        urlresponse = urllib2.urlopen(urlreq)
        the_page = urlresponse.read()
        jsonreturn = json.loads(the_page)
        if T_Member.objects.filter(UserID=jsonreturn['UserId'], IsUsed=True).count() == 0:
            T_Member.objects.create(
                UserID=jsonreturn['UserId'], IsUsed=True)
        member = T_Member.objects.get(UserID=jsonreturn['UserId'])
        if T_Admin.objects.filter(MemberId=member).count() != 0:
            list = []
            for admin in T_Admin.objects.filter(MemberId=member):
                list.append(admin.Department_ID)
            projects = T_Project.objects.filter(Department_ID__in=list)
            response=render_to_response('project/projectlist.html', {"level": "admin", "projects": projects})
        else:
            projectmembers = T_ProjectMember.objects.filter(MemberId=member)
            list = []
            for pmber in projectmembers:
                list.append(pmber.ProjectId.id)
            projects = T_Project.objects.filter(id__in=list)
            response=render_to_response('project/projectlist.html', {"level": "member", "projects": projects})
        response.set_cookie('userid', jsonreturn['UserId'])
        return response
    else:
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


def projectindex(req):
    # 项目列表
    return render_to_response('project/promanage.html', {'id':req.GET.get('id')})


def projectadd(req):
    # 添加项目
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    if req.method == 'GET':
        admins = T_Admin.objects.filter(MemberId=member)
        dejsons = getDepartmentList()
        for admin in admins:
            for dejson in dejsons:
                if admin.Department_ID == dejson['id']:
                    setattr(admin, 'Departmentname', dejson['name'])
        return render_to_response('project/projectadd.html', {'admins': admins})
    else:
        with transaction.atomic():
            pro = T_Project.objects.create(AdminId=T_Admin.objects.get(MemberId=member, Department_ID=int(req.POST.get('Department_ID', '1'))), Department_ID=int(req.POST.get('Department_ID', '1')), ProjectName=req.POST.get(
                'ProjectName'), ProjectDescribe=req.POST.get('ProjectDescribe'),
                ProjectStatus=req.POST.get('ProjectStatus'))
        return HttpResponse(str(pro.id))


def projectmem(req):
    # 设置项目成员
    if req.method == 'GET':
        projectid = req.GET.get('id')
        departmentid = T_Project.objects.get(id=projectid).Department_ID
        List = []
        for member in T_Member.objects.all():
            if int(departmentid) in member.memberinfo['department']:
                List.append(member.id)
        members = T_Member.objects.filter(id__in=List)
        for onemember in members:
            setattr(onemember, 'name', onemember.memberinfo['name'])
            setattr(onemember, 'ismember', '0')
            setattr(onemember, 'isheader', '0')
            if T_ProjectMember.objects.filter(ProjectId=T_Project.objects.get(id=projectid), MemberId=onemember).count() != 0:
                setattr(onemember, 'ismember', '1')
                if T_ProjectMember.objects.get(ProjectId=T_Project.objects.get(id=projectid), MemberId=onemember).isHead == True:
                    setattr(onemember, 'isheader', '1')
        return render_to_response('project/promember.html', {'id': projectid, 'members': members})
    else:
        with transaction.commit_on_success():
            projectid = req.POST.get('id')
            T_ProjectMember.objects.filter(
                ProjectId=T_Project.objects.get(id=projectid)).delete()
            members = req.POST.get('members').split(',')
            headers = req.POST.get('headers').split(',')
            for memberid in members:
                isheader = False
                if memberid in headers:
                    isheader = True
                T_ProjectMember.objects.create(ProjectId=pro, AdminId=T_Admin.objects.get(MemberId=member, Department_ID=int(
                    req.POST.get('Department_ID', '1'))), MemberId=T_Member.objects.get(UserID=memberid), isHead=isheader)
            return HttpResponse('success')


def projectdetail(req):
    # 项目详情页面
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    if req.method == 'GET':
        admin = T_Admin.objects.filter(MemberId=member, Department_ID=T_Project.objects.get(id=req.GET.get('id')).Department_ID)
        projectid = req.GET.get('id')
        project = T_Project.objects.get(id=projectid)
        if admin.count() != 0:#(T_Module.objects.filter(ProjectId=project).count() == 0) & (admin.count() != 0):
            return render_to_response('project/projectdetail.html', {'project': project, 'change': '1'})
        else:
            return render_to_response('project/projectdetail.html', {'project': project, 'change': '0'})
    else:
        admin = T_Admin.objects.get(MemberId=member, Department_ID=T_Project.objects.get(id=req.POST.get('id')).Department_ID)
        project = T_Project.objects.get(id=req.POST.get('id'))
        project.AdminId = admin
        project.Department_ID = req.POST.get('Department_ID')
        project.ProjectName = req.POST.get('ProjectName')
        project.ProjectDescribe = req.POST.get('ProjectDescribe')
        project.ProjectStatus = req.POST.get('ProjectStatus')
        project.save()
        return HttpResponse(project.id)


def moduleindex(req):
    #模块列表
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    project=T_Project.objects.get(id=req.GET.get('id'))
    modulelist=T_Module.objects.filter(ProjectId=project)
    projectmember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
    if ((T_Admin.objects.filter(MemberId=member,Department_ID=T_Project.objects.get(
        id=req.GET.get('id')).Department_ID).count() != 0) | projectmember.isHead)&(T_Demand.objects.filter(ModuleId__in=modulelist).count()==0):
        return render_to_response('module/modulelist.html', {"level": "admin","id":req.GET.get('id'),"modulelist": modulelist})
    else:
        return render_to_response('module/modulelist.html', {"level": "member", "id":req.GET.get('id'),"modulelist": modulelist})

def addmodule(req):
    #添加模块
    if req.method=='POST':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project=T_Project.objects.get(id=req.POST.get('id'))
        projectmember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
        T_Module.objects.create(ProjectMemberId=projectmember,ProjectId=project,ModuleName=req.POST.get('ModuleName'),Level=int(req.POST.get('Level')))
        return HttpResponse('success')
    elif req.method=='GET':
        return render_to_response('module/moduleadd.html',{'id':req.GET.get('id')})

def deletemodule(req):
    #删除模块
    module=T_Module.objects.get(id=req.GET.get('id'))
    if T_Demand.objects.filter(ModuleId=module).count()==0:
        module.delete()
        return HttpResponse('success')
    else:
        return HttpResponse('failure')

def moduledetail(req):
    #模块详情页
    if req.method=='GET':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project=T_Project.objects.get(id=req.GET.get('id'))
        module=T_Module.objects.get(id=req.GET.get('id'))
        projectmember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
        if ((T_Admin.objects.filter(MemberId=member,Department_ID=T_Project.objects.get(id=req.GET.get('id')).Department_ID).count() != 0) | projectmember.isHead)&(T_Demand.objects.filter(ModuleId=module).count()==0):
            return render_to_response('module/moduledetail.html',{'module':module,'isheader':'1'})
        else:
            return render_to_response('module/moduledetail.html',{'module':module,'isheader':'0'})
    else:
        module=T_Module.objects.get(id=req.GET.get('id'))
        if T_Demand.objects.filter(ModuleId=module).count()==0:
            module.ModuleName=req.POST.get('ModuleName')
            module.Level=int(req.POST.get('Level'))
            module.save()
            return HttpResponse('success')
        else:
            return HttpResponse('failure')

def demandlist(req):
#需求列表页
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    project=T_Project.objects.get(id=req.GET.get('id'))
    modules=T_Module.objects.filter(ProjectId=project)
    demands=T_Demand.objects.filter(ModuleId__in=modules).order_by('DemandStatus','Level')
    promember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
    if promember.isHead:
        return render_to_response('demand/demandlist.html',{'demands':demands,'isheader':'1',"id":req.GET.get('id')})
    else:
        return render_to_response('demand/demandlist.html',{'demands':demands,'isheader':'0',"id":req.GET.get('id')})

def demandadd(req):
    #需求添加
    if req.method=='POST':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project=T_Project.objects.get(id=req.POST.get('id'))
        projectmember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
        module=T_Module.objects.get(id=req.POST.get('meduleid'))
        T_Demand.objects.create(ProjectMemberId=projectmember,ModuleId=module,DemandName=req.POST.get('DemandName'),DemandStatus=req.POST.get('DemandStatus'),Level=int(req.POST.get('Level')),DemandDescribe=req.POST.get('DemandDescribe'))
        return HttpResponse('success')
    elif req.method=='GET':
        project=T_Project.objects.get(id=req.GET.get('id'))
        modules=T_Module.objects.filter(ProjectId=project)
        return render_to_response('demand/demandadd.html',{'id':req.GET.get('id'),'modules':modules})

def demanddelete(req):
    #删除需求
    print req.GET.get('demandid')
    T_Demand.objects.get(id=req.GET.get('demandid')).delete()
    return HttpResponseRedirect('/demandlist/?id='+req.GET.get('id'))

def demanddetail(req):
    #需求详情
    if req.method=='GET':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project=T_Project.objects.get(id=req.GET.get('id'))
        modules=T_Module.objects.filter(ProjectId=project)
        projectmember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
        demand=T_Demand.objects.get(id=req.GET.get('demandid'))
        if projectmember.isHead:
            return render_to_response('demand/demanddetail.html',{'demand':demand,'isheader':'1','modules':modules,"id":req.GET.get('id')})
        else:
            return render_to_response('demand/demanddetail.html',{'demand':demand,'isheader':'0','modules':modules,"id":req.GET.get('id')})
    elif req.method=='POST':
        module=T_Module.objects.get(id=req.POST.get('meduleid'))
        demand=T_Demand.objects.get(id=req.POST.get('demandid'))
        demand.ModuleId=module
        demand.DemandName=req.POST.get('DemandName')
        demand.DemandStatus=req.POST.get('DemandStatus')
        demand.Level=int(req.POST.get('Level'))
        demand.DemandDescribe=req.POST.get('DemandDescribe')
        demand.save()
        return HttpResponseRedirect('/demandlist/?id='+req.POST.get('id'))

def documentlist(req):
    #文档列表页
    project=T_Project.objects.get(id=req.GET.get('id'))
    documents=T_Document.objects.filter(ProjectId=project)
    return render_to_response('document/documentlist.html',{'documents':documents,"id":req.GET.get('id')})

def adddocument(req):
    #文档添加页面
    if req.method=='GET':
        return render_to_response('document/adddocument.html',{'id':req.GET.get('id')})
    else:
        reqfile = req.FILES['file']
        name=str(time.strftime('%Y%m%d%H%M%S'))
        path=os.path.join(basePath,"webStatic/upload/"+name+req.POST.get('filename'))
        project=T_Project.objects.get(id=req.POST.get('id'))
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        projectmember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
        with open(path, 'wb+') as destination:
            for chunk in ExcelUpload.chunks():
                destination.write(chunk)
        T_Document.objects.create(ProjectMemberId=projectmember,ProjectId=project,DocumentName=req.POST.get('DocumentName'),DocumentUrl=path)
        return HttpResponseRedirect('/documentlist/?id='+req.POST.get('id'))

def deletedocument(req):
    #文档删除
    T_Document.objects.get(id=req.GET.get('documentid')).delete()
    return HttpResponseRedirect('/documentlist/?id='+req.GET.get('id'))

def documentdetail(req):
    #文档详情
    if req.method=='GET':
        document=T_Document.objects.get(id=req.GET.get('documentid'))
        name=document.ProjectMemberId.MemberId.memberinfo['name']
        setattr(document,'uploader',name)
        return render_to_response('document/documentdetail.html',{'document':document,'id':req.GET.get('id')})
    else:
        reqfile = req.POST['file']
        name=str(time.strftime('%Y%m%d%H%M%S'))
        path=os.path.join(basePath,"webStatic/upload/"+name+req.POST.get('filename'))
        project=T_Project.objects.get(id=req.POST.get('id'))
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        projectmember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
        with open(path, 'wb+') as destination:
            for chunk in ExcelUpload.chunks():
                destination.write(chunk)
        document=T_Document.objects.get(id=req.POST.get('documentid'))
        document.ProjectMemberId=projectmembers
        document.DocumentName=req.POST.get('DocumentName')
        document.DocumentUrl=path
        document.save()
        return HttpResponseRedirect('/documentlist/?id='+req.POST.get('id'))

def testlist(req):
    #测试列表
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    project=T_Project.objects.get(id=req.GET.get('id'))
    modules=T_Module.objects.filter(ProjectId=project)
    tests=T_Test.objects.filter(ModuleId__in=modules).order_by('-TestStartTime')
    promember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
    if promember.isHead:
        return render_to_response('test/testlist.html',{'isheader':'1','tests':tests,"id":req.GET.get('id')})
    else:
        return render_to_response('test/testlist.html',{'isheader':'0','tests':tests,"id":req.GET.get('id')})

def testdetail(req):
    #测试详情
    if req.method=='GET':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project=T_Project.objects.get(id=req.GET.get('id'))
        test=T_Test.objects.get(id=req.GET.get('testid'))
        modules=T_Module.objects.filter(ProjectId=project)
        promember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
        if promember.isHead && test.TestStatus!='已完成':
            return render_to_response('test/testdetail.html',{'modules':modules,'test':test,'isheader':'1',"id":req.GET.get('id')})
        else:
            return render_to_response('test/testdetail.html',{'modules':modules,'test':test,'isheader':'0',"id":req.GET.get('id')})
    else:
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project=T_Project.objects.get(id=req.POST.get('id'))
        test=T_Test.objects.get(id=req.POST.get('testid'))
        promember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
        test.TestContent=req.POST.get('TestContent')
        test.TestName=req.POST.get('TestName')
        test.TestStatus=req.POST.get('TestStatus')
        test.save()
        return HttpResponseRedirect('/testlist/?id='+req.POST.get('id'))

def deletetest(req):
    #测试删除
    if T_Bug.objects.filter(TestId=T_Test.objects.get(id=req.GET.get('testid'))).count()==0:
        T_Test.objects.get(id=req.GET.get('testid')).delete()
    return HttpResponseRedirect('/testlist/?id='+req.GET.get('id'))

def addtest(req):
    #测试添加
    if req.method == 'GET':
        project=T_Project.objects.get(id=req.GET.get('id'))
        modules=T_Module.objects.filter(ProjectId=project)
        return render_to_response('/test/testadd.html',{'id':req.GET.get('id'),'modules':modules})
    else:
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project=T_Project.objects.get(id=req.POST.get('id'))
        promember=T_ProjectMember.objects.get(ProjectId=project,MemberId=member)
        module=T_Module.objects.get(id=req.POST.get('ModuleId'))
        T_Test.objects.create(ModuleId=module,ProjectMemberId=promember,TestName=req.POST.get('TestName'),TestContent=req.POST.get('TestContent'),TestStatus=req.POST.get('TestStatus'))
        return HttpResponseRedirect('/testlist/?id='+req.POST.get('id'))