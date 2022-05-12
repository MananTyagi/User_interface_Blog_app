#this for customize user creation forms in django
# our requirements are email address in user creation forms but not
# it is not given by default so we have ti customize it here
# adn then import from this file
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.models import Profile

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model =User
        fields = ['username','email','password1','password2']
        
        
        
#for updating user information
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']