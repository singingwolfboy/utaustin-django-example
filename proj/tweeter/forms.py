from django import forms

class TweetForm(forms.Form):
    tweet = forms.CharField(label='Tweet', max_length=140)
