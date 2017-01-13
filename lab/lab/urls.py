from django.conf.urls import include, url
from django.contrib import admin
from labmanage.views import *
from labmanage.enviews import *
from lab.uploads import upload_image
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    url(r'^admin/', include(admin.site.urls),name = 'manage'),
    url(r"^uploads/(?P<path>.*)$", \
        "django.views.static.serve", \
        {"document_root": settings.MEDIA_ROOT,}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^$', 'labmanage.views.home', name='home'),
    url(r'^news/','labmanage.views.news',name = 'news'),
    url(r'^news(?P<id>\d+)/','labmanage.views.detail',name = 'detail'),
    url(r'^person/','labmanage.views.person',name = 'person'),
    url(r'^student/','labmanage.views.student',name = 'student'),
    url(r'^field/','labmanage.views.field',name = 'field'),
    url(r'^field(?P<id>\d+)/','labmanage.views.fielddetail',name = 'fielddetail'),
    url(r'^achieve/','labmanage.views.achieve',name = 'achieve'),
    url(r'^paper/','labmanage.views.paper',name = 'paper'),
    url(r'^patent/','labmanage.views.patent',name = 'patent'),
    url(r'^technology/','labmanage.views.technology',name = 'technology'),
    url(r'^technology(?P<id>\d+)/','labmanage.views.engindetail',name = 'engindetail'),
    url(r'^about/','labmanage.views.about',name = 'about'),
    url(r'^device/','labmanage.views.device',name = 'device'),
    # url(r'^home/', ArticleListView.as_view(), name='blog_index'),
    # english
    url(r'^en/$', 'labmanage.enviews.home', name='enhome'),
    url(r'^en/news/','labmanage.enviews.news',name = 'ennews'),
    url(r'^en/news(?P<id>\d+)/','labmanage.enviews.detail',name = 'endetail'),
    url(r'^en/person/','labmanage.enviews.person',name = 'enperson'),
    url(r'^en/student/','labmanage.enviews.student',name = 'enstudent'),
    url(r'^en/field/','labmanage.enviews.field',name = 'enfield'),
    url(r'^en/field(?P<id>\d+)/','labmanage.enviews.fielddetail',name = 'enfielddetail'),
    url(r'^en/achieve/','labmanage.enviews.achieve',name = 'enachieve'),
    url(r'^en/paper/','labmanage.enviews.paper',name = 'enpaper'),
    url(r'^en/patent/','labmanage.enviews.patent',name = 'enpatent'),
    url(r'^en/technology/','labmanage.enviews.technology',name = 'entechnology'),
    url(r'^en/technology(?P<id>\d+)/','labmanage.enviews.engindetail',name = 'enengindetail'),
    url(r'^en/about/','labmanage.enviews.about',name = 'enabout'),
    url(r'^en/device/','labmanage.enviews.device',name = 'endevice'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
