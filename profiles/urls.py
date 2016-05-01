from django.conf.urls import patterns, include, url

urlpatterns = patterns('profiles.views',
    url(r'^home$', 'home', name='profiles_home')
)