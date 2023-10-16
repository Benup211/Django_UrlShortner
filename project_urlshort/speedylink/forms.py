from django import forms

class SigninForm(forms.Form):
    username=forms.CharField(label='username')
    password=forms.CharField(label='password')

class SignupForm(forms.Form):
    username=forms.CharField(label='username')
    email=forms.CharField(label='email')
    password=forms.CharField(label='password')