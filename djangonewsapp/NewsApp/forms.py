from django import forms
from .models import RegisterUser

class RegisterUserForm(forms.Form):
    username=forms.CharField(max_length=50,
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Username'
    }))
    password=forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Password',
        'type':'password'
    }))
    email=forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Email',
        'type':'email'
    }))
    phone=forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Phone'
    }))

class RegisterModel(forms.ModelForm):
    class Meta:
        model=RegisterUser
        fields=[
            'username',
            'password',
            'email',
            'phone'
        ]

        widgets = {
            'username':forms.TextInput(attrs={
            'class':'form-control',
            'placeholder':'Username'
            }),
            'password':forms.TextInput(attrs={
            'class':'form-control',
            'type':'password',
            'placeholder':'password'
            }), 
            'email':forms.TextInput(attrs={
            'class':'form-control',
            'type':'email',
            'placeholder':'email'
            }), 
            'phone':forms.TextInput(attrs={
            'class':'form-control',
            'type':'number',
            'placeholder':'Phone'
            }), 
        }