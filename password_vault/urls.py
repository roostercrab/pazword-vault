from django.urls import include, path

from . import views
from .views import (VaultCreateView, VaultDeleteView,
                    VaultDetailView, VaultListView,
                    VaultUpdateView,)


#password_vault urls
urlpatterns = [                    
    path('all_vaults/', VaultListView.as_view(), name='all-vaults'),
    path('vault_create/<class_id>/', VaultCreateView.as_view(), name='vault-create'),
    path('vault/<int:pk>/', VaultDetailView.as_view(), name='vault-detail'),
    path('vault/<int:pk>/delete/', VaultDeleteView.as_view(), name='vault-delete'),
    path('vault/<int:pk>/update/', VaultUpdateView.as_view(), name='vault-update'),
]