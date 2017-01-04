from django.conf.urls import url
from tweeter import views

urlpatterns = [
    url(
        r'users/(?P<username>\w+)$',
        views.UserProfileView.as_view(),
        name='user_profile',
    ),
    url(r'search/(?P<query>.+)$', views.search_results, name='search_results'),
    url(r'search$', views.search, name='search'),

    url(r'tweets$', views.tweet_list_json, name='tweet_list_json'),
    url(r'tweet/(?P<tweet_id>\d+)$', views.tweet_json, name='tweet_json'),
    # url(r'tweets$', views.TweetListView.as_view(), name='tweet_list'),
    url(r'tweet$', views.new_tweet, name='new_tweet'),
    url(r'$', views.home_page, name='home_page'),
]
