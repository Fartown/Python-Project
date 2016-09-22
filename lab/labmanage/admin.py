from django.contrib import admin
from labmanage.models import *

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )
admin.site.register(Funds, ArticleAdmin)
admin.site.register(Paper, ArticleAdmin)
admin.site.register(Engineer, ArticleAdmin)
admin.site.register(Student,ArticleAdmin)
admin.site.register(Patent, ArticleAdmin)
admin.site.register(News, ArticleAdmin)
admin.site.register(Field, ArticleAdmin)