from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns("",
    (r'^facebook/', include('django_facebook.urls')),
    url(r"^$", direct_to_template, {"template": "homepage.html"}, name="home"),
    url(r"^admin/", include(admin.site.urls)),

    url(r"^account/", include("account.urls")),
    url(r"^gen/", include("lessongen.apps.generator.urls")),
    #url(r"^accounts/", include("lessongen.apps.app.urls")),#used by social_auth
    (r'^accounts/', include('django_facebook.auth_urls')),
    url(r'', include('social_auth.urls')),
)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
