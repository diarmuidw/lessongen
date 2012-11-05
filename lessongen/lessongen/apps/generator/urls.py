from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
                       url(r"^$",'generator.views.gen_simple_math', name='gen_simple_math_direct'),
    url(r'^simple_math/$', 'generator.views.gen_simple_math', name='gen_simple_math'),
    url(r'^simple_image/$', 'generator.views.gen_images', name='gen_simple_image'),

)
