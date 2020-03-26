from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    """
    Form to be used to log exisitng users in
    """

    logInUsername = forms.CharField(label="Username or Email")
    password = forms.CharField(min_length=6, widget=forms.PasswordInput)
   
class UserRegistrationForm(UserCreationForm):
    """
    Form used to register new user
    """
  
    password1 = forms.CharField(
                    min_length=6,
                    label="Password",
                    widget=forms.PasswordInput)
                 
    password2 = forms.CharField(
                    min_length=6,
                    label="Password Confirmation", 
                    widget=forms.PasswordInput)
   
    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']
   
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')

        if not email:
            raise forms.ValidationError("Please provide your email address")
      
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'This email address is already registered')
        return email
     
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
           
        if password1 != password2:
            raise forms.ValidationError("Both passwords do not match")