from django.conf.urls import url
from tweeter import views

urlpatterns = [
    url(
        r'users/(?P<username>\w+)',
        views.UserProfileView.as_view(),
        name='user_profile',
    ),
    url(r'tweets', views.TweetListView.as_view(), name='tweet_list'),
    url(r'tweet', views.new_tweet, name='new_tweet'),
    url(r'', views.home_page, name='home_page'),
]
