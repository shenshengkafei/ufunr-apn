from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^validuser/$', views.validuser, name='validuser'),
    url(r'^expireduser/$', views.expireduser, name='expireduser'),
    url(r'^(?P<account_id>[0-9]+)/(?P<valid_days>[0-9]+)/(?P<data_left>[-]?[0-9]+\.[0-9]+)/(?P<is_deleted>[A-Z]+)/updateuserinfo$', views.updateuserinfo, name='updateuserinfo'),
]
