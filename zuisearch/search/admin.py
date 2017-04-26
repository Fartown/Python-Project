from django.contrib import admin
from search.models import *
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from django.contrib.admin import AdminSite #更改admin登录url和header
from django.contrib.auth.models import User
# from django.contrib.auth.models import Group

# Register your models here.
class SiteAdmin(admin.ModelAdmin):
    list_display = ('title', 'wxname', 'wbname', 'activate')
    search_fields = ('title', 'wxname', 'wbname')
    list_filter = ('column', 'activate')
    fieldsets = (
        ('网站', {
            'classes': ('grp-collapse grp-closed',),
            'fields': ('column', ('title', 'siteurl'), 'introduce',)
        }),
        ('微信', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (('wxname', 'wxid'), ('wxintro', 'wxcode'),)
        }),
        ('微博', {
            'classes': ('grp-collapse grp-closed',),
            'fields': (('wbname', 'wburl'),)
        }),
        ('优先级', {
            'classes': ('collapse',),
            'fields': (('priority', 'activate'),)
        }),
    )
class HomeAdmin(admin.ModelAdmin):
    list_display = ('title', 'siteurl', 'position')
    list_filter = ('position',)
class MyAdminSite(AdminSite):
    site_header = '醉搜索'
    site_title = '醉晚亭-醉搜索'
    index_title = '醉搜索管理'
admin_site = MyAdminSite(name='zuilogin')
admin_site.register(Site, SiteAdmin)
admin_site.register(Home, HomeAdmin)
admin_site.register(Column)
admin_site.register(User, UserAdmin)
# admin_site.register(Group, GroupAdmin)