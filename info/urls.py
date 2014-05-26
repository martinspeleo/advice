from django.conf.urls import patterns, include, url

urlpatterns = patterns('',    
    url(r'^$', 'info.views.home', name='home'),
)
