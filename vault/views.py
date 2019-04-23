from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .forms import PasswordForm
from .models import Password


class PasswordCreateView(LoginRequiredMixin, CreateView): 
    model = Password
    context_object_name = 'password'
    fields = [
        'saved_password',
        'website',
        'description',
        ]


class PasswordListView(ListView):
    model = Password
    template_name = 'passwords/all_passwords'
    context_object_name = 'passwords'


class PasswordDetailView(DetailView):
    model = Password


class PasswordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Password
    fields = [

        ]


class PasswordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Password
    success_url = '/all_passwords'