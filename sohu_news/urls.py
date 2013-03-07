from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.views.generic.simple import direct_to_template
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'news.views.news_by_time_mako'),
    url(r'^cate/', 'news.views.news_by_cate_mako'),
    url(r'^detail/(\d+)/$', 'news.views.news_detail_mako'),
    url(r'^newslike/(\d+)$', 'news.views.news_like'),
    url(r'^newsdislike/(\d+)$', 'news.views.news_dislike'),
    url(r'^about/$', 'news.views.about'),
    url('^404test/$', direct_to_template, {'template': '404.html'}),
    # url(r'^sohu_news/', include('sohu_news.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
