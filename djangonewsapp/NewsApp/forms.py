from django import forms

class RegisterUserForm(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(max_length=50)
    email=forms.CharField(max_length=50)
    phone=forms.CharField(max_length=50)