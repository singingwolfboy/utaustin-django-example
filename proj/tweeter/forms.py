from django import forms
from tweeter.models import Profile


class TweetForm(forms.Form):
    tweet = forms.CharField(label='Tweet', max_length=140)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
