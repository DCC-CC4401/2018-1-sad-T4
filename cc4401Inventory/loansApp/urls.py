from django.urls import path
from . import views

urlpatterns = [
    path('delete/space/', views.delete_space_reservation, name='delete_space_reservation'),
    path('delete/article/', views.delete_article_reservation, name='delete_article_reservation'),
    path('show/space/<int:reservation_id>', views.show_space_loan, name='show_space_loan'),
    path('show/article/<int:reservation_id>', views.show_article_loan, name='show_article_loan'),
]
