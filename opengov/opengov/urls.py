from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

from ehealt import views as ehealth_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'opengov.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^health/', ehealth_views.index),
)
