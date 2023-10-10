from django.urls import path

from .views import get_start_page, add_new_car, get_error_page, Choose_auto

app_name = 'main'
urlpatterns = [
    path('', get_start_page, name='main_page'),
    path('add_new_car/', add_new_car, name='add_new_car'),
    path('form_template/', Choose_auto.as_view(), name='form_template'),
    path('error/', get_error_page)
]