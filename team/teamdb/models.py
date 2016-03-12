# -*- coding: utf-8 -*-
#coding=utf-8
from django.db import models


#成员表
class T_Member(models.Model):
    UserID=models.CharField(unique=True,max_length=50, verbose_name='成员账号（企业号内必须唯一）')
    MemberName=models.CharField(max_length=100, verbose_name='成员姓名')
    PictureUrl=models.CharField(max_length=200, verbose_name='头像图片路径')
    IsUsed=models.BooleanField(verbose_name='该账号是否被删除')
    IsSuAdmin=models.BooleanField(verbose_name='是否为超级管理员')

    def __str__(self):
        return self.MemberName

#备忘录表
class T_Memo(models.Model):
    MemberId=models.ForeignKey(T_Member, verbose_name='成员id')
    MimoContent=models.TextField(blank=True,null=True, verbose_name='备忘录内容')
    CreateTime=models.DateTimeField(auto_now=True, verbose_name='创建时间')

    def __str__(self):
        return self.MimoContent

#论坛话题表
class T_Topic(models.Model):
    MemberId=models.ForeignKey(T_Member, verbose_name='创建人id')
    TopicContent=models.TextField(verbose_name='话题内容')
    CreateTime=models.DateTimeField(auto_now=True, verbose_name='创建时间')
    Department_ID=models.CharField(max_length=50, verbose_name='部门id')

    def __str__(self):
        return self.TopicContent

#话题回复表
class T_TopicReply(models.Model):
    MemberId=models.ForeignKey(T_Member, verbose_name='成员id')
    ReplyContent=models.TextField(verbose_name='回复内容')
    Level=models.IntegerField(verbose_name='回复楼层')
    CreateTime=models.DateTimeField(auto_now=True, verbose_name='回复时间')

    def __str__(self):
        return self.ReplyContent

#部门子管理员表
class T_Admin(models.Model):
    MemberId=models.ForeignKey(T_Member, verbose_name='成员id')
    Department_ID=models.CharField(max_length=50, verbose_name='部门id')

    def __str__(self):
        return self.MemberId.MemberName

#投票表
class T_Vote(models.Model):
    MemberId=models.ForeignKey(T_Member, verbose_name='创建人id')
    VoteContent=models.TextField(verbose_name='话题内容')
    CreateTime=models.DateTimeField(auto_now=True, verbose_name='创建时间')
    Department_ID=models.CharField(max_length=50, verbose_name='部门id')

    def __str__(self):
        return self.VoteContent

#投票选项表
class T_VoteOptions(models.Model):
    VoteId=models.ForeignKey(T_Vote, verbose_name='投票id')
    OptionContent=models.TextField(verbose_name='选项内容')
    OptionNum=models.IntegerField(verbose_name='投票人数')

    def __str__(self):
        return self.OptionContent

#项目表
class T_Project(models.Model):
    AdminId=models.ForeignKey(T_Admin, verbose_name='创建该项目的子部门管理员')
    ProjectName=models.CharField(max_length=100, verbose_name='项目名称')
    ProjectStartTime=models.DateTimeField(verbose_name='项目开始时间')
    ProjectEndTime=models.DateTimeField(verbose_name='预计项目结束时间')
    ProjectDescribe=models.TextField(blank=True,null=True, verbose_name='项目描述')
    ProjectStatus=models.CharField(max_length=50, verbose_name='项目当前状态')

    def __str__(self):
        return self.ProjectName

#项目组成员表
class T_ProjectMember(models.Model):
    ProjectId=models.ForeignKey(T_Project, verbose_name='项目id')
    AdminId=models.ForeignKey(T_Admin, verbose_name='加入该程序员的管理员id')
    MemberId=models.ForeignKey(T_Member, verbose_name='成员id')
    isHead=models.BooleanField(verbose_name='是否为项目负责人')

    def __str__(self):
        return self.MemberId.MemberName

#文档表
class T_Document(models.Model):
    ProjectMemberId=models.ForeignKey(T_ProjectMember, verbose_name='创建文档项目组成员id')
    DocumentName=models.CharField(max_length=50, verbose_name='文档名称')
    DocumentUrl=models.CharField(max_length=100, verbose_name='文档路径')

    def __str__(self):
        return self.DocumentName

#模块表
class T_Module(models.Model):
    ProjectMemberId=models.ForeignKey(T_ProjectMember, verbose_name='创建人id')
    ModuleName=models.CharField(max_length=50, verbose_name='模块名称')
    Level=models.IntegerField(verbose_name='模块优先级')

    def __str__(self):
        return self.ModuleName

#测试表
class T_Test(models.Model):
    ModuleId=models.ForeignKey(T_Module, verbose_name='测试所属模块')
    ProjectMemberId=models.ForeignKey(T_ProjectMember, verbose_name='创建测试的项目组成员id')
    TestName=models.CharField(max_length=100, verbose_name='测试名称')
    TestContent=models.TextField(verbose_name='测试内容')
    TestStatus=models.CharField(max_length=50, verbose_name='测试状态')
    TestStartTime=models.DateTimeField(auto_now=True, verbose_name='测试开始时间')
    TestEndTime=models.DateTimeField(auto_now=True, verbose_name='预计测试结束时间')

    def __str__(self):
        return self.TestName
#BUG表
class T_Bug(models.Model):
    ModuleId=models.ForeignKey(T_Module, verbose_name='bug所属模块')
    ProjectMemberId=models.ForeignKey(T_ProjectMember, verbose_name='提出bug项目组成员id')
    TestId=models.ForeignKey(T_Test,blank=True,null=True, verbose_name='bug所属测试（可为空）')
    Level=models.IntegerField(verbose_name='bug等级')
    BugStatus=models.CharField(max_length=50, verbose_name='bug当前状态')
    BugTitle=models.CharField(max_length=100, verbose_name='bug标题')
    BugContent=models.TextField(verbose_name='bug具体内容')

    def __str__(self):
        return self.BugTitle
#项目需求表
class T_Demand(models.Model):
    ModuleId=models.ForeignKey(T_Module, verbose_name='所属模块id')
    ProjectMemberId=models.ForeignKey(T_ProjectMember, verbose_name='创建成员id')
    DemandName=models.CharField(max_length=100, verbose_name='需求名称')
    DemandDescribe=models.TextField(verbose_name='需求描述')
    Level=models.IntegerField(verbose_name='优先级')
    DemandStatus=models.CharField(max_length=50, verbose_name='需求状态')

    def __str__(self):
        return self.DemandName

#需求bug更新日志
class T_DemandBugLog(models.Model):
    ProjectMemberId=models.ForeignKey(T_ProjectMember, verbose_name='更新日志的项目组成员id')
    BugId=models.ForeignKey(T_Bug,blank=True,null=True, verbose_name='bug的id')
    DemandId=models.ForeignKey(T_Demand,blank=True,null=True, verbose_name='需求id')
    LogContent=models.TextField(verbose_name='日志内容')

    def __str__(self):
        return self.LogContent

#需求指派表
class T_DemandAssigned(models.Model):
    ProjectMemberId=models.ForeignKey(T_ProjectMember, verbose_name='指派项目组成员id')
    BugId=models.ForeignKey(T_Bug,blank=True,null=True, verbose_name='Bugid(bugid和需求id二者有一个即可)')
    DemandId=models.ForeignKey(T_Demand,blank=True,null=True, verbose_name='需求id')

    def __str__(self):
        return self.ProjectMemberId.MemberId.MemberName

#日志表
class T_Log(models.Model):
    ProjectMemberId=models.ForeignKey(T_ProjectMember, verbose_name='项目成员id')
    LogContent=models.CharField(max_length=50, verbose_name='操作内容，根据xml记录')
    CreateTime=models.DateTimeField(auto_now=True, verbose_name='操作时间')

    def __str__(self):
        return self.LogContent