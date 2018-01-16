from django import forms
from django.contrib.auth.models import User
from aliexpress.models import TrackedList


class UserLoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'password']


class TrackedProduct(forms.ModelForm):
    class Meta:
        model = TrackedList
        fields = ['product']
