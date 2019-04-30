from crispy_forms.bootstrap import Field, InlineRadios, Tab, TabHolder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Fieldset, Layout, Submit
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms import ModelForm
from django.urls import reverse

# from django_zxcvbn.fields import PasswordField
# from zxcvbn_password import zxcvbn
# from zxcvbn_password.fields import PasswordConfirmationField, PasswordField

from .models import Password


class PasswordForm(ModelForm):
    class Meta:
        model = Password
        fields = [
        'saved_password',
        'website',
        'description',
        ]   


# class RegisterForm(forms.Form):
#     password1 = PasswordField()
#     password2 = PasswordConfirmationField(confirm_with='password1')

#     def clean(self):
#         password = self.cleaned_data.get('password1')
#         # other_field1 = ...
#         # other_field2 = ...

#         if password:
#             score = zxcvbn(password)['score']
#             # score = zxcvbn(password, [other_field1, other_field2])['score']
#             # score is between 0 and 4
#             # raise forms.ValidationError if needed

#         return self.cleaned_data
