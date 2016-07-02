# -*- coding: utf-8 -*-
#coding=utf-8
import os
from django.conf.urls import include, url
from django.conf.urls.static import static
from team.settings import STATICFILES_DIRS
from public.views import index,menu,deleteMenu
from bbs.views import *
from django.contrib import admin

urlpatterns = [
        url(r'^admin/', include(admin.site.urls)),
        url(r'^webStatic/(?P<path>.*)$','django.views.static.serve',{'document_root':STATICFILES_DIRS[0],'show_indexes':True}),
       url(r'^templates/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),'../templates').replace('\\','/'),'show_indexes':True}),
      url(r'^$',index),
      url(r'^menu/$',menu),
        #平台管理
      url(r'^people/$',people),
      url(r'^peopleDepartment/$',peopleDepartment),
      url(r'^peoplemanage/$',peoplemanage),
      url(r'^addmessage/$',addmessage),
      url(r'^addDepartment/$',addDepartment),
      url(r'^addPeople/$',addPeople),
        #项目管理
      url(r'^project/$',project),
      url(r'^projectindex/$',projectindex),
      url(r'^projectadd/$',projectadd),
      url(r'^projectdetail/$',projectdetail),
      url(r'^projectmem/$',projectmem),
      url(r'^moduleindex/$',moduleindex),
      url(r'^addmodule/$',addmodule),
      url(r'^deletemodule/$',deletemodule),
      url(r'^moduledetail/$',moduledetail),
      url(r'^demandlist/$',demandlist),
      url(r'^demandadd/$',demandadd),
      url(r'^demanddelete/$',demanddelete),
      url(r'^demanddetail/$',demanddetail),
      url(r'^documentlist/$',documentlist),
      url(r'^adddocument/$',adddocument),
      url(r'^deletedocument/$',deletedocument),
      url(r'^documentdetail/$',documentdetail),
      url(r'^testlist/$',testlist),
      url(r'^testdetail/$',testdetail),
      url(r'^deletetest/$',deletetest),
      url(r'^addtest/$',addtest),
      url(r'^buglist/$',buglist),
      url(r'^bugadd/$',bugadd),
      url(r'^bugadd2/$',bugdetail),
      url(r'^bugdelete/$',bugdelete),
      url(r'^bugdetail/$',bugdetail),
      url(r'^assignlist/$',assignlist),
      url(r'^deleteassign/$',deleteassign),
      url(r'^addassign/$',addassign),
      url(r'^assigndetail/$',assigndetail),
      url(r'^loglist/$',loglist),
      url(r'^report/$',report),
        #畅言论坛
      url(r'^bbs/$',bbs),
      url(r'^bbslist/$',bbslist),
      url(r'^addbbs/$',addbbs),
      url(r'^bbsdetail/$',bbsdetail),
      url(r'^votelist/$',votelist),
      url(r'^addvote/$',addvote),
      url(r'^votedetail/$',votedetail),
        #备忘录
      url(r'^memo/$',MemoTemplateView.as_view(), name='memoindex'),
      url(r'^addmemo/$',addmemo),
      url(r'^memodetail/$',memodetail),
      url(r'^deletememo/$',deletememo),
]
