from django.urls import path
from . import views

urlpatterns = [
    path('delete/', views.delete, name='delete_reservation'),
    path('modify-spaceReservations/', views.modify_spaceReservations, name="modify_spaceReservations"),
    path('modify-ArticleReservations/', views.modify_articleReservations, name="modify_articleReservations"),
    path('show/<int:reservation_id>', views.show, name='show_reservation'),
    path('delete/space/', views.delete_space_reservation, name='delete_space_reservation'),
    path('delete/article/', views.delete_article_reservation, name='delete_article_reservation'),
    path('modify/', views.modify_reservations, name="modify_reservations"),
    path('show/space/<int:reservation_id>', views.show_space_reservation, name='show_space_reservation'),
    path('show/article/<int:reservation_id>', views.show_article_reservation, name='show_article_reservation'),
]
