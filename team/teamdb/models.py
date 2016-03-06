# -*- coding: utf-8 -*-
#coding=utf-8
from django.db import models


#成员表
class T_Member(models.Model):
    UserID=models.CharField(max_length=50)
    MemberName=models.CharField(max_length=100)
    PictureUrl=models.CharField(max_length=200)
    IsUsed=models.BooleanField()
    IsSuAdmin=models.BooleanField()

#备忘录表
class T_Memo(models.Model):
    MemberId=models.ForeignKey(T_Member)
    MimoContent=models.TextField(blank=True,null=True)
    CreateTime=models.DateTimeField(auto_now=True)

#论坛话题表
class T_Topic(models.Model):
    MemberId=models.ForeignKey(T_Member)
    TopicContent=models.TextField()
    CreateTime=models.DateTimeField(auto_now=True)
    Department_ID=models.CharField(max_length=50)

#话题回复表
class T_TopicReply(models.Model):
    MemberId=models.ForeignKey(T_Member)
    ReplyContent=models.TextField()
    Level=models.IntegerField()
    CreateTime=models.DateTimeField(auto_now=True)

#部门子管理员表
class T_Admin(models.Model):
    MemberId=models.ForeignKey(T_Member)
    Department_ID=models.CharField(max_length=50)

#投票表
class T_Vote(models.Model):
    MemberId=models.ForeignKey(T_Member)
    VoteContent=models.TextField()
    CreateTime=models.DateTimeField(auto_now=True)
    Department_ID=models.CharField(max_length=50)

#投票选项表
class T_VoteOptions(models.Model):
    VoteId=models.ForeignKey(T_Vote)
    OptionContent=models.TextField()
    OptionNum=models.IntegerField()

#项目表
class T_Project(models.Model):
    AdminId=models.ForeignKey(T_Admin)
    ProjectName=models.CharField(max_length=100)
    ProjectStartTime=models.DateTimeField()
    ProjectEndTime=models.DateTimeField()
    ProjectDescribe=models.TextField(blank=True,null=True)
    ProjectStatus=models.CharField(max_length=50)

#项目组成员表
class T_ProjectMember(models.Model):
    ProjectId=models.ForeignKey(T_Project)
    AdminId=models.ForeignKey(T_Admin)
    MemberId=models.ForeignKey(T_Member)
    isHead=models.BooleanField()

#文档表
class T_Document(models.Model):
    ProjectMemberId=models.ForeignKey(T_ProjectMember)
    DocumentName=models.CharField(max_length=50)

#模块表
class T_Module(models.Model):
    ProjectMemberId=models.ForeignKey(T_ProjectMember)
    ModuleName=models.CharField(max_length=50)
    Level=models.IntegerField()

#测试表
class T_Test(models.Model):
    ModuleId=models.ForeignKey(T_Module)
    ProjectMemberId=models.ForeignKey(T_ProjectMember)
    TestName=models.CharField(max_length=100)
    TestContent=models.TextField()
    TestStatus=models.CharField(max_length=50)
    TestStartTime=models.DateTimeField(auto_now=True)
    TestEndTime=models.DateTimeField(auto_now=True)

#BUG表
class T_Bug(models.Model):
    ModuleId=models.ForeignKey(T_Module)
    ProjectMemberId=models.ForeignKey(T_ProjectMember)
    TestId=models.ForeignKey(T_Test,blank=True,null=True)
    Level=models.IntegerField()
    BugStatus=models.CharField(max_length=50)
    BugTitle=models.CharField(max_length=100)
    BugContent=models.TextField()

#项目需求表
class T_Demand(models.Model):
    ModuleId=models.ForeignKey(T_Module)
    ProjectMemberId=models.ForeignKey(T_ProjectMember)
    DemandName=models.CharField(max_length=100)
    DemandDescribe=models.TextField()
    Level=models.IntegerField()
    DemandStatus=models.CharField(max_length=50)

#需求bug更新日志
class T_DemandBugLog(models.Model):
    ProjectMemberId=models.ForeignKey(T_ProjectMember)
    BugId=models.ForeignKey(T_Bug,blank=True,null=True)
    DemandId=models.ForeignKey(T_Demand,blank=True,null=True)
    LogContent=models.TextField()

#需求指派表
class T_DemandAssigned(models.Model):
    ProjectMemberId=models.ForeignKey(T_ProjectMember)
    BugId=models.ForeignKey(T_Bug,blank=True,null=True)
    DemandId=models.ForeignKey(T_Demand,blank=True,null=True)

#日志表
class T_Log(models.Model):
    ProjectMemberId=models.ForeignKey(T_ProjectMember)
    LogContent=models.CharField(max_length=50)
    CreateTime=models.DateTimeField(auto_now=True)