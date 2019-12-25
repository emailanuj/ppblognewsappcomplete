from django import forms

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