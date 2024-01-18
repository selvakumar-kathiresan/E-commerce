from django import forms
from django.contrib.auth.forms import UserCreationForm
from applite.models import User

class CustomUserForm(UserCreationForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
	email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your password'}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter conform password'}))
	class Meta:
		model=User
		fields=['username','email','password1','password2']
