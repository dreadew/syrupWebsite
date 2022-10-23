from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.airtable, name="airtable"),
    path('delete/<str:pk>', views.delete, name="airtable-delete"),
    path('create/', views.create, name="airtable-create"),
    path('edit/<str:pk>', views.edit, name="airtable-edit")
]