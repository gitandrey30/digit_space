from django.urls import path

from .views import get_start_page

app_name = 'main'
urlpatterns = [
    path('', get_start_page),
]