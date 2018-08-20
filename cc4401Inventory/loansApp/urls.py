from django.urls import path
from . import views

urlpatterns = [
    path('show/space/<int:reservation_id>', views.show_space_loan, name='show_space_loan'),
    path('show/article/<int:reservation_id>', views.show_article_loan, name='show_article_loan'),
]
