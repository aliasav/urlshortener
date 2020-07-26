'''Contains all URLs for web app of project
'''
from django.conf.urls import url
from web import views
from web import api

urlpatterns = [

    # home page url
    url(r'^home/$', views.home_view, name="home_view"),

    # url(r'^base/$', views.base_view),

    # redirect view
    url(r'r/(?P<hash_value>\w+)/$', views.redirect_view),

    # get API
    url(r'_api/v1/url-detail/(?P<hash_value>\w+)/$', api.URLDetailAPI.as_view()),

    # post API
    url(r'_api/v1/url-create/$', api.URLDetailAPI.as_view()),
]