from django.conf.urls import include, url
from django.contrib import admin
from labmanage.views import *
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
    url(r'^home/', ArticleListView.as_view(), name='blog_index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
