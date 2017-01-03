from django.conf.urls import url
from tweeter import views

urlpatterns = [
    url(r'', views.home_page, name='home_page'),
]
