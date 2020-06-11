from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name="all_actions_url"),
    path('add/', add_action, name="add_action_url"),
    path('delete/', delete_action, name="delete_action_url"),
]
