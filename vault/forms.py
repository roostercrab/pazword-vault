from crispy_forms.bootstrap import Field, InlineRadios, Tab, TabHolder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Fieldset, Layout, Submit
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms import ModelForm
from django.urls import reverse

from .models import Password


class PasswordForm(ModelForm):
    class Meta:
        model = Password
        fields = [
        'saved_password',
        'website',
        'description',
        ]   