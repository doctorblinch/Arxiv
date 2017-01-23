from django.conf.urls import url

from . import views

app_name = 'arxiv'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^main/$', views.main, name = 'main'),
	url(r'^(?P<article_id>[0-9]+)/$', views.detail, name='detail'),
]
