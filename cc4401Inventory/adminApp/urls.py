from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_panel, name="landing-panel"),
    path('user-panel/', views.user_panel, name="user-panel"),
    path('items-panel/', views.items_panel, name="items-panel"),
    path('actions-panel/', views.actions_panel, name="actions-panel"),
    path('items-panel/add-item/', views.add_item, name="add-item")
]
