from django.conf.urls import patterns, include, url
import profiles.views

urlpatterns = [
    url(r'^home$', profiles.views.home,
    name='profiles_home'),
]