from django.urls import path
from . import views

urlpatterns = [
    path('delete/<int:space_id>', views.space_delete, name='space_delete'),
    path('<int:space_id>', views.space_data, name='space_data'),
    path('<int:space_id>/edit_name', views.space_edit_name, name='space_edit_name'),
    path('<int:space_id>/edit_image', views.space_edit_image, name='space_edit_image'),
    path('<int:space_id>/edit_description', views.space_edit_description, name='space_edit_description'),
]
