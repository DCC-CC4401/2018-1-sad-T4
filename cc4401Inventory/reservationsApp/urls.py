from django.urls import path
from . import views

urlpatterns = [
    path('delete/', views.delete, name='delete_reservation'),
    path('modify/', views.modify_reservations, name="modify_reservations"),
    path('show/space/<int:reservation_id>', views.show_space_reservation, name='show_space_reservation'),
    path('show/article/<int:reservation_id>', views.show_article_reservation, name='show_article_reservation'),
]
