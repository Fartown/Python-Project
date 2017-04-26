from django.conf.urls import include, url
# from django.contrib import admin
from search.admin import admin_site
from search.views import *
from django.conf import settings
from django.conf.urls.static import static
# from haystack.views import SearchView
urlpatterns = [
    # Examples:
    # url(r'^$', 'zuisearch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^uploads/(?P<path>.*)$', "django.views.static.serve", {'document_root': settings.MEDIA_ROOT}, name="photo"),
    url(r'^zuilogin/', include(admin_site.urls)),
    url(r'^$', 'search.views.home', name='index'),
    url(r'^home/', 'search.views.home', name='home'),
    url(r'^gate/', 'search.views.nav', name='nav'),
    url(r'^detail/(?P<id>\d+)/', 'search.views.detail', name='detail'),
    url(r'^search/', include('haystack.urls')),
]
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
