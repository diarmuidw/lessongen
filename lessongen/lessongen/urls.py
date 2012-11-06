from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns("",
    
    #url(r"^$", direct_to_template, {"template": "homepage.html"}, name="home"),
    url(r"^$",include("lessongen.apps.generator.urls")),
    (r'^facebook/', include('django_facebook.urls')),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^account/", include("account.urls")),
    url(r"^gen/", include("lessongen.apps.generator.urls")),
    #url(r"^accounts/", include("lessongen.apps.app.urls")),#used by social_auth
    (r'^accounts/', include('django_facebook.auth_urls')),
    url(r'', include('social_auth.urls')),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
Various FB auth mechanism were evaluated with django_facebook being a clear winner
It allows relatively easy setup and allows posting to wall, etc
Social_auth was used and worked but is just for authentication and while it allows 
integration with twitter, etc FB integration will do for now.

A CSRF error was happening on the facebook canvas page (as it should) because the
template was being rendered directly. This home page 



'''