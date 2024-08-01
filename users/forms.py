from django import forms

from users.models import CustomUser


class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email','profile_picture')

class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password',)