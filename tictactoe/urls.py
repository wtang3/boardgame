from django.conf.urls import patterns, include, url
import tictactoe.views

urlpatterns = [
    url(r'^invites$', tictactoe.views.new_invitation,
    name='tictactoe_invite'),
]