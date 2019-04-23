from django.urls import include, path

from . import views
from .views import (PasswordCreateView, PasswordDeleteView,
                    PasswordDetailView, PasswordListView,
                    PasswordUpdateView,)


#password urls
urlpatterns = [                    
    path('password_list/', PasswordListView.as_view(), name='password-list'),
    path('password_create/', PasswordCreateView.as_view(), name='password-create'),
    path('password/<int:pk>/', PasswordDetailView.as_view(), name='password-detail'),
    path('password/<int:pk>/delete/', PasswordDeleteView.as_view(), name='password-delete'),
    path('password/<int:pk>/update/', PasswordUpdateView.as_view(), name='password-update'),
]