from django.conf.urls import url
from tweeter import views

urlpatterns = [
    url(r'users/(?P<username>\w+)', views.view_user, name='view_user'),
    url(r'tweet', views.new_tweet, name='new_tweet'),
    url(r'', views.home_page, name='home_page'),
]
