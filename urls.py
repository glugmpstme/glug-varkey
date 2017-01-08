from django.conf.urls import url
from . import views


app_name = 'blog' #namespacing
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<slug>[^\.]+)/$', views.post, name='post'),
]
