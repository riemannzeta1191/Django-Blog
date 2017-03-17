from django import  forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']





# class UserRegisterForm(forms.Form):
#     usrname = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)



# class UserLogoutForm(forms.Form):
#     usrname = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#