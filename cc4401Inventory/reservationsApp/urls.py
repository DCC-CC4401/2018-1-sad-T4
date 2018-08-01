from django.urls import path
from . import views

urlpatterns = [
    path('delete/', views.delete, name='delete_reservation'),
    path('modify/', views.modify_reservations, name="modify_reservations"),
]
