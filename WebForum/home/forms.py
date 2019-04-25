from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    username = forms.CharField(
        max_length=20,
        required=True,
        help_text="Required. Max 20 characters."
        )
    first_name = forms.CharField(
        max_length=50,
        required=True,
        help_text="Required. 50 characters or fewer."
        )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        help_text="Required. 50 characters or fewer."
        )
    email = forms.EmailField(
        max_length=150,
        help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'
        )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
