from django import forms
from account.models import Account
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm




class SignUpForm(forms.ModelForm):
    password1 = forms.CharField(
        label = "Password",
        widget=forms.PasswordInput(
        attrs={
            'placeholder':'Password',
            'class':'form-control-s',
        }))


    password2 = forms.CharField(
        label = "Password Confirm",
        widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password(again)',
        'class':'form-control-s',
    }))


    class Meta:
        model = Account
        fields = ['first_name','last_name','email',"age"]


        widgets     = {
            'first_name':forms.TextInput(attrs={'placeholder':'First Name','class':'form-control-s'}),
            'last_name':forms.TextInput(attrs={'class':'form-control-s','placeholder':'Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control-s','placeholder':'Enter Email'}),
            'age':forms.TextInput(attrs={'class':'form-control-s','placeholder':'Enter your Age'})
        }



    def clean(self):
        cleaned_data        = super(SignUpForm,self).clean()
        password            = cleaned_data.get('password')
        confirm_password    = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("password does not match !")
        return 

class UserProfileUpdateForm(SignUpForm):
    password1 = None
    password2 = None

    class Meta:
        model = Account
        fields = ['first_name','last_name','email',"age"]

        widgets     = {
            'first_name':forms.TextInput(attrs={'placeholder':'First Name','class':'form-control-s'}),
            'last_name':forms.TextInput(attrs={'class':'form-control-s','placeholder':'Last Name'}),
            'email':forms.EmailInput(attrs={'class':'form-control-s','placeholder':'Enter Email','type':'hidden'}),
            'age':forms.TextInput(attrs={'class':'form-control-s','placeholder':'Enter your Age'})
        }
