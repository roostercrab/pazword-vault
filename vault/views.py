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

    def get_success_url(self, *args, **kwargs):
        password_id = self.kwargs['password_id']
        print(password_id)
        return reverse('password-detail', kwargs={'pk': password_id})

class PasswordListView(ListView):
    model = Password
    template_name = 'passwords/all_passwords'
    context_object_name = 'passwords'


class PasswordDetailView(DetailView):
    model = Password


class PasswordUpdateView(LoginRequiredMixin, UpdateView):
    model = Password
    fields = [
        'saved_password',
        'website',
        'description',
        ]

    def form_valid(self, form):
        return super().form_valid(form)

        
class PasswordDeleteView(LoginRequiredMixin, DeleteView):
    model = Password
    success_url = '/vault/password_list'