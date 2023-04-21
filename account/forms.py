from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserForm(UserCreationForm):
    password1 = forms.CharField(max_length=16,widget =forms.PasswordInput(attrs={'placeholder':'Password','class':'flex-g'}))  
    password2 = forms.CharField(max_length=16,widget =forms.PasswordInput(attrs={'placeholder':'Confirm Password'})) 
    
    class Meta:
        model = User
        fields = ('first_name','username','email','password1','password2')
        widgets = {
            'first_name' : forms.TextInput(attrs={'placeholder':'Name'}),
            'username' : forms.TextInput(attrs={'placeholder':'Username'}),
            'email' : forms.EmailInput(attrs={'placeholder':'Email'}),
        }

        
