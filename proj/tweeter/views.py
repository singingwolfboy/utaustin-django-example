from __future__ import print_function

from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import Http404, HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.models import User
from django.contrib import messages
from django.views import View
from django.urls import reverse
from django.views.generic import ListView
from tweeter.models import Tweet, Profile
from tweeter.forms import TweetForm, UserProfileForm, SearchForm


@require_http_methods(["GET"])
def home_page(request):
    form = TweetForm()
    recent_tweets = Tweet.objects.order_by('-created_at').all()[:5]
    context = {
        "recent_tweets": recent_tweets,
        "form": form,
    }
    return render(request, "home_page.html", context)


class UserProfileView(View):

    def get_user(self, username):
        try:
            user = User.objects.filter(username=username).get()
        except User.DoesNotExist:
            raise Http404("User {username} not found".format(username=username))
        return user

    def get(self, request, username):
        user = self.get_user(username)

        if user == request.user:
            profile_form = UserProfileForm(instance=user.profile)
            tweet_form = TweetForm()
        else:
            profile_form = None
            tweet_form = None

        user_tweets = (
            Tweet.objects.filter(creator=user)
            .order_by('-created_at').all()
        )
        context = {
            "viewed_user": user,
            "tweets": user_tweets,
            "profile_form": profile_form,
            "tweet_form": tweet_form,
        }
        return render(request, "user_profile.html", context)

    def post(self, request, username):
        user = self.get_user(username)
        if user != request.user:
            return HttpResponseBadRequest("You can't modify another user's profile.")

        profile_form = UserProfileForm(request.POST, instance=user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Your profile has been updated.',
            )

        return HttpResponseRedirect(
            reverse('user_profile', kwargs={"username": user.username})
        )


@require_http_methods(["POST"])
def new_tweet(request):
    tweet_form = TweetForm(request.POST)
    if tweet_form.is_valid():
        tweet = tweet_form.save(commit=False)
        tweet.creator = request.user
        tweet.save()
        messages.add_message(
            request,
            messages.SUCCESS,
            'Your tweet has been posted!',
        )
    next_url = request.GET.get("next") or "/"
    return HttpResponseRedirect(next_url)


class TweetListView(ListView):
    queryset = Tweet.objects.order_by('-created_at')


@require_http_methods(["GET", "POST"])
def search(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data["query"]
            url = reverse("search_results", kwargs={"query": query})
            return HttpResponseRedirect(url)
    else:
        form = SearchForm()
    context = {
        "form": form,
    }
    return render(request, "search_form.html", context)


def search_results(request, query):
    results = Tweet.objects.filter(content__icontains=query).all()
    context = {
        "query": query,
        "search_results": results,
    }
    return render(request, "search_results.html", context)
