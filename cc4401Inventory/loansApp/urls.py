from django.urls import path
from . import views

urlpatterns = [
    path('show/<int:reservation_id>', views.show, name='show_loans'),
]
