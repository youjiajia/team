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
        url(r'^webStatic/(?P<path>.*)$','django.views.static.serve',{'document_root':STATICFILES_DIRS,'show_indexes':True}),
        url(r'^templates/(?P<path>.*)$','django.views.static.serve',{'document_root':os.path.join(os.path.dirname(__file__),'../templates').replace('\\','/'),'show_indexes':True}),
        url(r'^$',index),
        url(r'^menu/$',menu),
        #平台管理
        url(r'^people/$',people),
        #项目管理
        url(r'^project/$',project),
        #畅言论坛
        url(r'^bbs/$',bbs),
        #备忘录
        url(r'^memo/$',memo),
]
