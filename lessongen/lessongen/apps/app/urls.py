from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from lessongen.apps.app.views import home, done, logout, error, form, form2
from lessongen.apps.app.facebook import facebook_view
from lessongen.apps.app.vkontakte import vkontakte_view
from lessongen.apps.app.odnoklassniki import ok_app, ok_app_info

urlpatterns = patterns("",
    url(r'^$', home, name='homea'),
    url(r'^done/$', done, name='done'),
    url(r'^error/$', error, name='error'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^form/$', form, name='form'),
    url(r'^form2/$', form2, name='form2'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fb/', facebook_view, name='fb_app'),
    url(r'^vk/', vkontakte_view, name='vk_app'),
    url(r'^ok/$', ok_app , name='ok_app'),
    url(r'^ok/info/$', ok_app_info , name='ok_app_info'),
)
