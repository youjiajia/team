from django.contrib import admin
from models import *
# Register your models here.
admin.site.register(T_Member)
admin.site.register(T_Memo)
admin.site.register(T_Topic)
admin.site.register(T_TopicReply)
admin.site.register(T_Admin)
admin.site.register(T_Vote)
admin.site.register(T_VoteOptions)
admin.site.register(T_Project)
admin.site.register(T_ProjectMember)
admin.site.register(T_Document)
admin.site.register(T_Module)
admin.site.register(T_Test)
admin.site.register(T_Bug)
admin.site.register(T_Demand)
admin.site.register(T_DemandBugLog)
admin.site.register(T_DemandAssigned)
admin.site.register(T_Log)