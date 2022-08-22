from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('manual_search', views.manual_search),
    path('search_by_text_file', views.search_by_text_file)
]
