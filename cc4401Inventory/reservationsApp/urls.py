from django.urls import path
from . import views

urlpatterns = [
    path('delete/', views.delete, name='delete_reservation'),
    path('modify-spaceReservations/', views.modify_spaceReservations, name="modify_spaceReservations"),
    path('modify-ArticleReservations/', views.modify_articleReservations, name="modify_articleReservations"),
    path('show/<int:reservation_id>', views.show, name='show_reservation'),
]
