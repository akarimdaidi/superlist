from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^$', 'lists.views.home_page', name='home'),
	url(r'^lists/the_only_list_in_the_world/$', 'lists.views.list_view',
		name='view_list'),
]
