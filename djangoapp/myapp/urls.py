from django.urls import path
from . import views

urlpatterns = [
    path("", views.message_form_view, name="message_form"),
    path('form/', views.message_form_view, name='message_form'),
    path('table/', views.message_table_view, name='message_table'),
]
