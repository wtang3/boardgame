from django.conf.urls import patterns, include, url

#urlpatterns = patterns('profiles.views',
#    url(r'^home$', 'home', name='profiles_home')
#)

import profiles.views
import main.views

urlpatterns = [
    url(r'^$', profiles.views.home,
    name='profiles_home'),
]