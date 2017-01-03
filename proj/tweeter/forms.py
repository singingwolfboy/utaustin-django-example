from django import forms
from tweeter.models import Tweet, Profile


# class TweetForm(forms.Form):
#     tweet = forms.CharField(label='Tweet', max_length=140)

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
