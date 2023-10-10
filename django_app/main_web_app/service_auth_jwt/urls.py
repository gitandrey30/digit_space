from django.urls import path

from .views import registration, authentication, get_start_page

app_name = 'service_auth_jwt'
urlpatterns = [
    path('', get_start_page),
    path('registration/', registration, name='registration'),
    path('authentication/', authentication, name='authentication')
]