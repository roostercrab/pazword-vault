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

from .forms import VaultForm
from .models import Vault


class VaultCreateView(LoginRequiredMixin, CreateView): 
    model = Vault
    context_object_name = 'class'
    fields = [
        'name',
        'number',
        ]
 
    def get_context_data(self, **kwargs):
        context = super(VaultCreateView, self).get_context_data(**kwargs)
        class_id = self.kwargs['class_id']
        class_name_queryset = Class.objects.filter(pk=class_id).values('class_name')
        for name in class_name_queryset:
            class_name = name['class_name']
        context['class_name'] = class_name
        return context

    def form_valid(self, form, *args, **kwargs):
        class_id = self.kwargs['class_id']
        form.instance.class_id = Class(class_id)
        form.instance.who_created = self.request.user
        form.instance.who_modified = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('vault-detail', kwargs={'pk': self.object.pk})


class VaultListView(ListView):
    model = Vault
    template_name = 'vaults/all_vaults'
    context_object_name = 'vaults'


class VaultDetailView(DetailView):
    model = Vault
    context_object_name = 'class_id'


class VaultUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Vault
    fields = [
        'name',
        'number',
        'class_id',
        ]

    def form_valid(self, form):
        return super().form_valid(form)

    def test_func(self):
        update_vault = self.get_object()
        user = CuserMiddleware.get_user()
        if user.is_teacher or user.is_admin:
            return True
        return False


class VaultDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Vault
    success_url = '/classes/all_vaults'

    def test_func(self):
        update_vault = self.get_object()
        user = CuserMiddleware.get_user()
        if user.is_teacher or user.is_admin:
            return True
        return False