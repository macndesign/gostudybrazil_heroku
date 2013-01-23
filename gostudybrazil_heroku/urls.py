from django.contrib import admin
from django.conf.urls.defaults import patterns, include, url
# static imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


# See: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#hooking-adminsite-instances-into-your-urlconf
admin.autodiscover()


# See: https://docs.djangoproject.com/en/dev/topics/http/urls/
urlpatterns = patterns('',
    # Admin panel and documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    
    # Index
    url(r'^$', 'django.views.generic.simple.direct_to_template',
        {'template': 'index.html'}, name='index'),
        
    # About
    url(r'^about/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'about.html'}, name='about'),
    
    # Courses
    url(r'^courses/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'courses.html'}, name='courses'),
    
    # Blog
    url(r'^blog/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'blog.html'}, name='blog'),
    
    # Contact
    url(r'^contact/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'contact.html'}, name='contact'),
    
    # Programs
    url(r'^programs/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'programs.html'}, name='programs'),
    
    # Housing
    url(r'^housing/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'housing.html'}, name='housing'),
    
    # Partners
    url(r'^partners/$', 'django.views.generic.simple.direct_to_template',
        {'template': 'partners.html'}, name='partners'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
