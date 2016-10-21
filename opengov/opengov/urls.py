from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

from ehealt.views import hospital as hospital_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opengov.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^health/hospital/$', hospital_views.index),
    url(r'^health/hospital/add$', hospital_views.add),
    url(r'^health/hospital/(?P<hospital_id>\w+)$', hospital_views.detail),
    url(r'^health/hospital/edit/(?P<hospital_id>\w+)$', hospital_views.edit),
    url(r'^health/hospital/delete/(?P<hospital_id>\w+)$', hospital_views.delete),
)
