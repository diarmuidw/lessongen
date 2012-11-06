from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns("",
                       url(r"^$",'generator.views.homepage', name='home'),
    url(r'^simple_math/$', 'generator.views.gen_simple_math', name='gen_simple_math'),
    url(r'^simple_image/$', 'generator.views.gen_images', name='gen_simple_image'),
    url(r'^image/$', 'generator.views.image', name='gen_image'),
    url(r'^maze/$', 'generator.views.maze', name='gen_maze'),

)
