# -*- coding: utf-8 -*-
#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from public.models import WXBizMsgCrypt
import xml.etree.cElementTree as ET
import json
import StringIO
import os,base64
import time
import uuid
import urllib,urllib2
basePath=os.path.dirname(os.path.dirname(__file__))
logPath=os.path.join(basePath,"log/publicError.txt")
informationStateXml=os.path.join(basePath,"webStatic/xml/weiConfig.xml")
tree = ET.ElementTree(file=informationStateXml)
sToken = tree.find("sToken").text
sEncodingAESKey = tree.find("sEncodingAESKey").text
sCorpID = tree.find("sCorpID").text
sCorpSecret = tree.find("sCorpSecret").text
#获取access_token函数
@csrf_exempt
def getToken(CorpSecret):
	req = urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+sCorpID+'&corpsecret='+CorpSecret)
	response = urllib2.urlopen(req)
	the_page = response.read()
	return json.loads(the_page)['access_token']
# 首次验证视图
@csrf_exempt
def index(req):
	wxcpt=WXBizMsgCrypt(sToken,sEncodingAESKey,sCorpID)
	ret,sEchoStr=wxcpt.VerifyURL(req.GET["msg_signature"], req.GET["timestamp"],req.GET["nonce"],req.GET["echostr"])
	return HttpResponse(sEchoStr)
#自定义菜单视图
def menu(req):
	Token=getToken(sCorpSecret)
	url='https://qyapi.weixin.qq.com/cgi-bin/menu/create?access_token='+Token+'&agentid=2'
	requestStr='{"button":[{"name":"部门管理","sub_button":[{"type":"view","name":"添加部门","url":"http://210.31.198.175:3334"},{"type":"view","name":"删除部门","url":"http://210.31.198.175:3334"},{"type":"view","name":"查看及修改部门信息","url":"http://210.31.198.175:3334"}]},{"name":"标签管理","sub_button":[{"type":"view","name":"添加标签","url":"http://210.31.198.175:3334"},{"type":"view","name":"删除标签","url":"http://210.31.198.175:3334"},{"type":"view","name":"查看及修改标签信息","url":"http://210.31.198.175:3334"}]},{"name":"人员管理","sub_button":[{"type":"view","name":"新增成员","url":"http://210.31.198.175:3334"},{"type":"view","name":"批量导入","url":"http://210.31.198.175:3334"},{"type":"view","name":"成员查看和修改","url":"http://210.31.198.175:3334"}]}]}'
	req = urllib2.Request(url, requestStr)
	response = urllib2.urlopen(req)
	the_page = response.read()
	return HttpResponse(the_page)
#删除菜单
def deleteMenu(req):
	Token=getToken(sCorpSecret)
	url=urllib2.Request('https://qyapi.weixin.qq.com/cgi-bin/menu/delete?access_token='+Token+'&agentid=2')
	response=urllib2.urlopen(url)
	the_page=response.read()
	return HttpResponse(the_page)