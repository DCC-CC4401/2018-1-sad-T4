from django.urls import path

from . import views

urlpatterns = [
    path('delete/<int:space_id>', views.space_delete, name='space_delete'),
]
