from crispy_forms.bootstrap import Field, InlineRadios, Tab, TabHolder
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Div, Fieldset, Layout, Submit
from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.forms import ModelForm
from django.urls import reverse

from .models import Vault


class VaultForm(ModelForm):
    class Meta:
        model = Vault
        fields = [
        'class_name',
        'description',
        'expectations',
        'curriculum',
        ]   