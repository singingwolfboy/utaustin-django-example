from django.shortcuts import render
from tweeter.models import Tweet

def home_page(request):
    recent_tweets = Tweet.objects.order_by('-created_at').all()[:5]
    context = {
        "recent_tweets": recent_tweets,
    }
    return render(request, "home_page.html", context)
