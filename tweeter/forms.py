from django import forms
from tweeter.models import Tweet, Profile


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        labels = {
            "content": "Tweet"
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class SearchForm(forms.Form):
    query = forms.CharField()
