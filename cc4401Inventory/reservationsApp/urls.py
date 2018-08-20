from django.urls import path
from . import views

urlpatterns = [
    path('modify-spaceReservations/', views.modify_spaceReservations, name="modify_spaceReservations"),
    path('modify-ArticleReservations/', views.modify_articleReservations, name="modify_articleReservations"),
    path('delete/space/', views.delete_space_reservation, name='delete_space_reservation'),
    path('delete/article/', views.delete_article_reservation, name='delete_article_reservation'),
    path('show/space/<int:reservation_id>', views.show_space_reservation, name='show_space_reservation'),
    path('show/article/<int:reservation_id>', views.show_article_reservation, name='show_article_reservation'),
]
