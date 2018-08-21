from django.urls import path
from . import views

urlpatterns = [
    path('modify-reservations/', views.modify_reservations, name="modify_reservations"),
    path('modify-loans/', views.modify_loans, name="modify_loans"),
    path('delete/space/', views.delete_reservation, name='delete_reservation'),
    path('delete/article/', views.delete_reservation, name='delete_reservation'),
    path('show/space/<int:reservation_id>', views.show_space_reservation, name='show_space_reservation'),
    path('show/article/<int:reservation_id>', views.show_article_reservation, name='show_article_reservation'),
]
