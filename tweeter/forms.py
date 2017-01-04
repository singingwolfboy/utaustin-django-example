from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from tweeter.models import Tweet, Profile


class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.CharField(widget=widgets.EmailInput)
    password = forms.CharField(widget=widgets.PasswordInput)
    repeated_password = forms.CharField(widget=widgets.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        existing_user = User.objects.filter(username=username).first()
        if existing_user:
            raise forms.ValidationError("Username is already taken")
        return username

    # def clean_password(self):
    #     "I don't know what the problem is"
    #     password = self.cleaned_data['password']
    #     if password == "password":
    #         raise forms.ValidationError("Use something stronger")
    #     return password

    def clean(self):
        cleaned_data = super(UserRegistrationForm, self).clean()
        password = cleaned_data['password']
        repeated_password = cleaned_data['repeated_password']
        if password != repeated_password:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


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
