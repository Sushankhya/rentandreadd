from cProfile import label
from pyexpat import model
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 
from django import forms

class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels ={
            'email': 'Email',
            'password2': 'Confirm Password',
        }
        widgets = {
            'first_name': forms.TextInput(attrs = {'placeholder': 'First Name',  'autofocus': True}),
            'last_name': forms.TextInput(attrs = {'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs = {'placeholder': 'Username'}),
            'email': forms.TextInput(attrs = {'placeholder': 'Email'}),
        }
        # def __init__(self, *args, **kwargs):
        #     super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        #     self.fields['password1'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password from numbers and letters of the Latin alphabet'}),
        #     self.fields['password2'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})
        