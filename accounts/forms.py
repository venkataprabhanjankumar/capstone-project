from django import forms
from django.contrib.auth.hashers import make_password

from .models import Users


class LoginForm(forms.Form):
    username = forms.CharField(max_length=225, widget=forms.TextInput())
    password = forms.CharField(max_length=225, widget=forms.PasswordInput())


class SignUpForm(forms.ModelForm):
    def save(self, commit=True):  # overrides method save
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])
        user.is_staff = False
        user.is_superuser = False
        if commit:
            user.save()
        return user

    class Meta:
        model = Users
        fields = ('first_name', 'last_name', 'username', 'email', 'password',
                  'gender', 'profilePic')
        widgets = {
            'password': forms.PasswordInput(),
            'profilePic': forms.FileInput({'accept': 'image/png, image/gif, image/jpeg'})
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('profilePic', 'first_name', 'last_name', 'email', 'gender')
