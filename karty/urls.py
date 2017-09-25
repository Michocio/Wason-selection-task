from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.main, name='main'),
    url(r'^experimentator$', views.experimentator),
    url(r'^session/(?P<which>\d)/$', views.session),
    url(r'^info/(?P<phase>\d)/$', views.info),
    url(r'^user/(?P<pilotaz>\d)/$', views.user),
    url(r'^GIL_data$', views.data),
    url(r'^save_data$', views.save_data),
    url(r'^selection/(?P<mode>\d)/(?P<which>\d)/$', views.selection),
    url(r'^dane/$', views.dane, name='dane'),
    url(r'^data/(?P<id>.*)/$', views.excel, name='data'),
]
