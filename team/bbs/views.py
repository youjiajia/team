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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
            response = render_to_response(
                'project/projectlist.html', {"level": "admin", "projects": projects})
        else:
            projectmembers = T_ProjectMember.objects.filter(MemberId=member)
            list = []
            for pmber in projectmembers:
                list.append(pmber.ProjectId.id)
            projects = T_Project.objects.filter(id__in=list)
            response = render_to_response(
                'project/projectlist.html', {"level": "member", "projects": projects})
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
    return render_to_response('project/promanage.html', {'id': req.GET.get('id')})


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
        admin = T_Admin.objects.filter(MemberId=member, Department_ID=T_Project.objects.get(
            id=req.GET.get('id')).Department_ID)
        projectid = req.GET.get('id')
        project = T_Project.objects.get(id=projectid)
        # (T_Module.objects.filter(ProjectId=project).count() == 0) & (admin.count() != 0):
        if admin.count() != 0:
            return render_to_response('project/projectdetail.html', {'project': project, 'change': '1'})
        else:
            return render_to_response('project/projectdetail.html', {'project': project, 'change': '0'})
    else:
        admin = T_Admin.objects.get(MemberId=member, Department_ID=T_Project.objects.get(
            id=req.POST.get('id')).Department_ID)
        project = T_Project.objects.get(id=req.POST.get('id'))
        project.AdminId = admin
        project.Department_ID = req.POST.get('Department_ID')
        project.ProjectName = req.POST.get('ProjectName')
        project.ProjectDescribe = req.POST.get('ProjectDescribe')
        project.ProjectStatus = req.POST.get('ProjectStatus')
        project.save()
        return HttpResponse(project.id)


def moduleindex(req):
    # 模块列表
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    project = T_Project.objects.get(id=req.GET.get('id'))
    modulelist = T_Module.objects.filter(ProjectId=project)
    projectmember = T_ProjectMember.objects.get(
        ProjectId=project, MemberId=member)
    if ((T_Admin.objects.filter(MemberId=member, Department_ID=T_Project.objects.get(
            id=req.GET.get('id')).Department_ID).count() != 0) | projectmember.isHead) & (T_Demand.objects.filter(ModuleId__in=modulelist).count() == 0):
        return render_to_response('module/modulelist.html', {"level": "admin", "id": req.GET.get('id'), "modulelist": modulelist})
    else:
        return render_to_response('module/modulelist.html', {"level": "member", "id": req.GET.get('id'), "modulelist": modulelist})


def addmodule(req):
    # 添加模块
    if req.method == 'POST':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project = T_Project.objects.get(id=req.POST.get('id'))
        projectmember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        T_Module.objects.create(ProjectMemberId=projectmember, ProjectId=project, ModuleName=req.POST.get(
            'ModuleName'), Level=int(req.POST.get('Level')))
        return HttpResponse('success')
    elif req.method == 'GET':
        return render_to_response('module/moduleadd.html', {'id': req.GET.get('id')})


def deletemodule(req):
    # 删除模块
    module = T_Module.objects.get(id=req.GET.get('id'))
    if T_Demand.objects.filter(ModuleId=module).count() == 0:
        module.delete()
        return HttpResponse('success')
    else:
        return HttpResponse('failure')


def moduledetail(req):
    # 模块详情页
    if req.method == 'GET':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project = T_Project.objects.get(id=req.GET.get('id'))
        module = T_Module.objects.get(id=req.GET.get('id'))
        projectmember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        if ((T_Admin.objects.filter(MemberId=member, Department_ID=T_Project.objects.get(id=req.GET.get('id')).Department_ID).count() != 0) | projectmember.isHead) & (T_Demand.objects.filter(ModuleId=module).count() == 0):
            return render_to_response('module/moduledetail.html', {'module': module, 'isheader': '1'})
        else:
            return render_to_response('module/moduledetail.html', {'module': module, 'isheader': '0'})
    else:
        module = T_Module.objects.get(id=req.GET.get('id'))
        if T_Demand.objects.filter(ModuleId=module).count() == 0:
            module.ModuleName = req.POST.get('ModuleName')
            module.Level = int(req.POST.get('Level'))
            module.save()
            return HttpResponse('success')
        else:
            return HttpResponse('failure')


def demandlist(req):
    # 需求列表页
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    project = T_Project.objects.get(id=req.GET.get('id'))
    modules = T_Module.objects.filter(ProjectId=project)
    demands = T_Demand.objects.filter(
        ModuleId__in=modules).order_by('DemandStatus', 'Level')
    promember = T_ProjectMember.objects.get(ProjectId=project, MemberId=member)
    if promember.isHead:
        return render_to_response('demand/demandlist.html', {'demands': demands, 'isheader': '1', "id": req.GET.get('id')})
    else:
        return render_to_response('demand/demandlist.html', {'demands': demands, 'isheader': '0', "id": req.GET.get('id')})


def demandadd(req):
    # 需求添加
    if req.method == 'POST':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project = T_Project.objects.get(id=req.POST.get('id'))
        projectmember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        module = T_Module.objects.get(id=req.POST.get('meduleid'))
        T_Demand.objects.create(ProjectMemberId=projectmember, ModuleId=module, DemandName=req.POST.get('DemandName'), DemandStatus=req.POST.get(
            'DemandStatus'), Level=int(req.POST.get('Level')), DemandDescribe=req.POST.get('DemandDescribe'))
        return HttpResponse('success')
    elif req.method == 'GET':
        project = T_Project.objects.get(id=req.GET.get('id'))
        modules = T_Module.objects.filter(ProjectId=project)
        return render_to_response('demand/demandadd.html', {'id': req.GET.get('id'), 'modules': modules})


def demanddelete(req):
    # 删除需求
    print req.GET.get('demandid')
    T_Demand.objects.get(id=req.GET.get('demandid')).delete()
    return HttpResponseRedirect('/demandlist/?id=' + req.GET.get('id'))


def demanddetail(req):
    # 需求详情
    if req.method == 'GET':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project = T_Project.objects.get(id=req.GET.get('id'))
        modules = T_Module.objects.filter(ProjectId=project)
        projectmember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        demand = T_Demand.objects.get(id=req.GET.get('demandid'))
        if projectmember.isHead:
            return render_to_response('demand/demanddetail.html', {'demand': demand, 'isheader': '1', 'modules': modules, "id": req.GET.get('id')})
        else:
            return render_to_response('demand/demanddetail.html', {'demand': demand, 'isheader': '0', 'modules': modules, "id": req.GET.get('id')})
    elif req.method == 'POST':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project = T_Project.objects.get(id=req.POST.get('id'))
        projectmember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        demand = T_Demand.objects.get(id=req.GET.get('demandid'))
        module = T_Module.objects.get(id=req.POST.get('meduleid'))
        demand = T_Demand.objects.get(id=req.POST.get('demandid'))
        demand.ModuleId = module
        demand.DemandName = req.POST.get('DemandName')
        demand.DemandStatus = req.POST.get('DemandStatus')
        demand.Level = int(req.POST.get('Level'))
        demand.DemandDescribe = req.POST.get('DemandDescribe')
        demand.save()
        T_DemandBugLog.objects.create(
            ProjectMemberId=projectmember, DemandId=demand, LogContent='更新测试')
        return HttpResponseRedirect('/demandlist/?id=' + req.POST.get('id'))


def documentlist(req):
    # 文档列表页
    project = T_Project.objects.get(id=req.GET.get('id'))
    documents = T_Document.objects.filter(ProjectId=project)
    return render_to_response('document/documentlist.html', {'documents': documents, "id": req.GET.get('id')})


def adddocument(req):
    # 文档添加页面
    if req.method == 'GET':
        return render_to_response('document/adddocument.html', {'id': req.GET.get('id')})
    else:
        reqfile = req.read()
        name = str(time.strftime('%Y%m%d%H%M%S'))
        path = os.path.join(BASE_DIR, "webStatic/upload/" +
                            name + req.META.get('HTTP_FILENAME'))
        project = T_Project.objects.get(id=req.META.get('HTTP_ID'))
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        projectmember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        with open(path, 'wb+') as destination:
            destination.write(reqfile)
        T_Document.objects.create(ProjectMemberId=projectmember, ProjectId=project,
                                  DocumentName=req.META.get('HTTP_DOCUMENTNAME'), DocumentUrl=path)
        return HttpResponseRedirect('/documentlist/?id=' + req.META.get('HTTP_ID'))


def deletedocument(req):
    # 文档删除
    T_Document.objects.get(id=req.GET.get('documentid')).delete()
    return HttpResponseRedirect('/documentlist/?id=' + req.GET.get('id'))


def documentdetail(req):
    # 文档详情
    if req.method == 'GET':
        document = T_Document.objects.get(id=req.GET.get('documentid'))
        name = document.ProjectMemberId.MemberId.memberinfo['name']
        setattr(document, 'uploader', name)
        return render_to_response('document/documentdetail.html', {'document': document, 'id': req.GET.get('id')})
    else:
        reqfile = req.read()
        name = str(time.strftime('%Y%m%d%H%M%S'))
        path = os.path.join(BASE_DIR, "webStatic/upload/" +
                            name + req.META.get('HTTP_FILENAME'))
        project = T_Project.objects.get(id=req.META.get('HTTP_ID'))
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        projectmember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        with open(path, 'wb+') as destination:
            destination.write(reqfile)
        document = T_Document.objects.get(id=req.META.get('HTTP_DOCUMENTID'))
        document.ProjectMemberId = projectmembers
        document.DocumentName = req.META.get('HTTP_DOCUMENTNAME')
        document.DocumentUrl = path
        document.save()
        return HttpResponseRedirect('/documentlist/?id=' + req.META.get('HTTP_ID'))


def testlist(req):
    # 测试列表
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    project = T_Project.objects.get(id=req.GET.get('id'))
    modules = T_Module.objects.filter(ProjectId=project)
    tests = T_Test.objects.filter(
        ModuleId__in=modules).order_by('-TestStartTime')
    promember = T_ProjectMember.objects.get(ProjectId=project, MemberId=member)
    if promember.isHead:
        return render_to_response('test/testlist.html', {'isheader': '1', 'tests': tests, "id": req.GET.get('id')})
    else:
        return render_to_response('test/testlist.html', {'isheader': '0', 'tests': tests, "id": req.GET.get('id')})


def testdetail(req):
    # 测试详情
    if req.method == 'GET':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project = T_Project.objects.get(id=req.GET.get('id'))
        test = T_Test.objects.get(id=req.GET.get('testid'))
        modules = T_Module.objects.filter(ProjectId=project)
        promember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        if promember.isHead & test.TestStatus != '已完成':
            return render_to_response('test/testdetail.html', {'modules': modules, 'test': test, 'isheader': '1', "id": req.GET.get('id')})
        else:
            return render_to_response('test/testdetail.html', {'modules': modules, 'test': test, 'isheader': '0', "id": req.GET.get('id')})
    else:
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project = T_Project.objects.get(id=req.POST.get('id'))
        test = T_Test.objects.get(id=req.POST.get('testid'))
        promember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        test.TestContent = req.POST.get('TestContent')
        test.TestName = req.POST.get('TestName')
        test.TestStatus = req.POST.get('TestStatus')
        test.save()
        return HttpResponseRedirect('/testlist/?id=' + req.POST.get('id'))


def deletetest(req):
    # 测试删除
    if T_Bug.objects.filter(TestId=T_Test.objects.get(id=req.GET.get('testid'))).count() == 0:
        T_Test.objects.get(id=req.GET.get('testid')).delete()
    return HttpResponseRedirect('/testlist/?id=' + req.GET.get('id'))


def addtest(req):
    # 测试添加
    if req.method == 'GET':
        project = T_Project.objects.get(id=req.GET.get('id'))
        modules = T_Module.objects.filter(ProjectId=project)
        return render_to_response('/test/testadd.html', {'id': req.GET.get('id'), 'modules': modules})
    else:
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project = T_Project.objects.get(id=req.POST.get('id'))
        promember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        module = T_Module.objects.get(id=req.POST.get('ModuleId'))
        T_Test.objects.create(ModuleId=module, ProjectMemberId=promember, TestName=req.POST.get(
            'TestName'), TestContent=req.POST.get('TestContent'), TestStatus=req.POST.get('TestStatus'))
        return HttpResponseRedirect('/testlist/?id=' + req.POST.get('id'))


def buglist(req):
    # bug列表页
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    project = T_Project.objects.get(id=req.GET.get('id'))
    modules = T_Module.objects.filter(ProjectId=project)
    bugs = T_Bug.objects.filter(
        ModuleId__in=modules).order_by('BugStatus', 'Level')
    promember = T_ProjectMember.objects.get(ProjectId=project, MemberId=member)
    if promember.isHead:
        return render_to_response('bug/buglist.html', {'bugs': bugs, 'isheader': '1', "id": req.GET.get('id')})
    else:
        return render_to_response('bug/buglist.html', {'bugs': bugs, 'isheader': '0', "id": req.GET.get('id')})


def bugadd(req):
    # bug添加
    if req.method == 'POST':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project = T_Project.objects.get(id=req.POST.get('id'))
        projectmember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        module = T_Module.objects.get(id=req.POST.get('ModuleId'))
        if req.POST.get('TestId', '') == '':
            T_Bug.objects.create(ProjectMemberId=projectmember, ModuleId=module, Level=req.POST.get('Level'), BugStatus=req.POST.get(
                'BugStatus'), BugTitle=req.POST.get('BugTitle'), BugContent=req.POST.get('BugContent'))
        else:
            test = T_Test.objects.get(id=req.POST.get('TestId'))
            T_Bug.objects.create(ProjectMemberId=projectmember, TestId=test, ModuleId=module, Level=req.POST.get(
                'Level'), BugStatus=req.POST.get('BugStatus'), BugTitle=req.POST.get('BugTitle'), BugContent=req.POST.get('BugContent'))
        return HttpResponseRedirect('/buglist/?id=' + req.POST.get('id'))
    elif req.method == 'GET':
        project = T_Project.objects.get(id=req.GET.get('id'))
        modules = T_Module.objects.filter(ProjectId=project)
        tests = T_Test.objects.filter(ProjectId=project)
        return render_to_response('bug/bugadd.html', {'id': req.GET.get('id'), 'modules': modules, 'tests': test})


def bugdelete(req):
    # 删除bug
    print req.GET.get('bugid')
    T_Bug.objects.get(id=req.GET.get('bugid')).delete()
    return HttpResponseRedirect('/demandlist/?id=' + req.GET.get('id'))


def bugdetail(req):
    # bug详情
    if req.method == 'GET':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project = T_Project.objects.get(id=req.GET.get('id'))
        modules = T_Module.objects.filter(ProjectId=project)
        projectmember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        bug = T_Bug.objects.get(id=req.GET.get('bugid'))
        if projectmember.isHead:
            return render_to_response('bug/bugdetail.html', {'bug': bug, 'isheader': '1', 'modules': modules, "id": req.GET.get('id')})
        else:
            return render_to_response('bug/bugdetail.html', {'bug': bug, 'isheader': '0', 'modules': modules, "id": req.GET.get('id')})
    elif req.method == 'POST':
        member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
        project = T_Project.objects.get(id=req.POST.get('id'))
        projectmember = T_ProjectMember.objects.get(
            ProjectId=project, MemberId=member)
        bug = T_Demand.objects.get(id=req.GET.get('bugid'))
        module = T_Module.objects.get(id=req.POST.get('meduleid'))
        bug.BugStatus = req.POST.get('BugStatus')
        bug.BugTitle = req.POST.get('BugTitle')
        bug.BugContent = req.POST.get('BugContent')
        bug.save()
        T_DemandBugLog.objects.create(
            ProjectMemberId=projectmember, BugId=bug, LogContent='更新BUG')
        return HttpResponseRedirect('/bug/?id=' + req.POST.get('id'))

def assignlist(req):
    #任务列表
    member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
    project = T_Project.objects.get(id=req.GET.get('id'))
    promember = T_ProjectMember.objects.get(ProjectId=project, MemberId=member)
    demands=T_DemandAssigned.objects.filter(ProjectMemberId=promember).exclude(DemandId=None).order_by('-CreateTime')
    bugs=T_DemandAssigned.objects.filter(ProjectMemberId=promember).exclude(BugId=None).order_by('-CreateTime')
    if promember.isHead:
        return render_to_response('assign/assignlist.html', {'demands':demands,'bugs': bugs, 'isheader': '1', "id": req.GET.get('id')})
    else:
        return render_to_response('assign/assignlist.html', {'demands':demands,'bugs': bugs, 'isheader': '0', "id": req.GET.get('id')})

def deleteassign(req):
    #删除任务
    print req.GET.get('assignid')
    T_DemandAssigned.objects.get(id=req.GET.get('assignid')).delete()
    return HttpResponseRedirect('/assignlist/?id=' + req.GET.get('id'))

def addassign(req):
    #添加任务
    if req.method=='GET':
        project = T_Project.objects.get(id=req.GET.get('id'))
        modules = T_Module.objects.filter(ProjectId=project)
        demands=T_Demand.objects.filter(ModuleId__in=modules).filter(DemandStatus='未分配').order_by('Level')
        bugs=T_Bug.objects.filter(ModuleId__in=modules).filter(BugStatus='未分配').order_by('Level')
        members=T_ProjectMember.objects.filter(ProjectId=project)
        for member in members:
            name = members.MemberId.memberinfo['name']
            setattr(member,'name',name)
        return render_to_response('assign/assignadd.html',{'members':members,'demands':demands,'bugs':bugs,'id': req.GET.get('id')})
    else:
        members=req.POST.get('members').split(',')
        demand=None
        bug=None
        if req.POST.get('demandid','')!='':
            demand=T_Demand.objects.get(id=req.POST.get('demandid'))
        if req.POST.get('bugid','')!='':
            bug=T_Bug.objects.get(id=req.POST.get('bugid'))
        with transaction.commit_on_success():
            for member in members:
                if member !='' & member !=None:
                    T_DemandAssigned.objects.create(DemandId=demand,BugId=bug,ProjectMemberId=T_ProjectMember.objects.get(id=member))
        return HttpResponseRedirect('/assignlist/?id=' + req.POST.get('id'))

def assigndetail(req):
    if req.method=='GET':
        assign=T_DemandAssigned.objects.get(id=req.GET.get('assignid'))
        if assign.BugId!=None:
            logs=T_DemandBugLog.objects.filter(BugId=assign.BugId).order_by('-CreateTime')
            for log in logs:
                name = log.ProjectMemberId.MemberId.memberinfo['name']
                setattr(log,'name',name)
            return render_to_response('assign/assigndetail.html',{'type':'bug','assign':assign,'logs':logs,'id': req.GET.get('id')})
        elif assign.DemandId!=None:
            logs=T_DemandBugLog.objects.filter(DemandId=assign.DemandId).order_by('-CreateTime')
            for log in logs:
                name = log.ProjectMemberId.MemberId.memberinfo['name']
                setattr(log,'name',name)
            return render_to_response('assign/assigndetail.html',{'type':'demand','assign':assign,'logs':logs,'id': req.GET.get('id')})
    else:
        if req.POST.get('type')=='bug':
            with transaction.commit_on_success():
                member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
                project = T_Project.objects.get(id=req.POST.get('id'))
                promember = T_ProjectMember.objects.get(ProjectId=project, MemberId=member)
                assign=T_DemandAssigned.objects.get(id=req.POST.get('assignid'))
                T_DemandBugLog.objects.create(ProjectMemberId=promember,BugId=assign.BugId,LogContent=req.POST.get('LogContent'))
                assign.BugId.BugStatus=req.POST.get('status')
                assign.BugId.save()
                return HttpResponseRedirect('/assignlist/?id=' + req.POST.get('id'))
        else:
            with transaction.commit_on_success():
                member = T_Member.objects.get(UserID=req.COOKIES.get('userid'))
                project = T_Project.objects.get(id=req.POST.get('id'))
                promember = T_ProjectMember.objects.get(ProjectId=project, MemberId=member)
                assign=T_DemandAssigned.objects.get(id=req.POST.get('assignid'))
                T_DemandBugLog.objects.create(ProjectMemberId=promember,DemandId=assign.DemandId,LogContent=req.POST.get('LogContent'))
                assign.DemandId.DemandStatus=req.POST.get('status')
                assign.DemandId.save()
                return HttpResponseRedirect('/assignlist/?id=' + req.POST.get('id'))

def loglist(req):
    logs=T_Log.objects.all()
    for log in logs:
        name = log.ProjectMemberId.MemberId.memberinfo['name']
        setattr(log,'name',name)
    return render_to_response('log/loglist.html',{'logs':logs})