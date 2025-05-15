from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(label='Имэйл хаяг')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Хэрэглэгчийн нэр'
        self.fields['password1'].label = 'Нууц үг'
        self.fields['password2'].label = 'Нууц үг давтах'

        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = 'Хамгийн багадаа 8 тэмдэгт урт байх ёстой.'
        self.fields['password2'].help_text = 'Нууц үгээ дахин оруулна уу.'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        labels = {
            'username': 'Хэрэглэгчийн нэр',
            'email': 'Имэйл хаяг',
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address', 'phone', 'image']
        labels = {
            'address': 'Хаяг',
            'phone': 'Утас',
            'image': 'Зураг',
        }
