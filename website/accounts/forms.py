from django import forms
from registration.forms import RegistrationForm
from .models import User


class CustomUserForm(RegistrationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'faculty', 'phone_number',]


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'faculty', 'phone_number',]
        # widgets = {
        #     'username': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'value': 'username',
        #     }),
        #     'first_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'value': 'first_name',
        #     }),
        #     'last_name': forms.TextInput(attrs={
        #         'class': 'form-control',
        #         'value': 'last_name',
        #     })
        # }
        # exclude = ()