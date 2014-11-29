from django.conf.urls import patterns, include, url

from django.contrib import admin
from app1 import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^news/', views.PostsAll),
)
