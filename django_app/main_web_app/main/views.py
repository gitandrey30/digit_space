from django.shortcuts import render, redirect
from django.urls import path
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.views.generic import ListView, TemplateView

from .form import NewCarForm, ChooseCarForm
from .models import ModelOfCar


def get_start_page(request):
    return render(request, 'main.html', {'title': 'main_page'})


def add_new_car(request):
    if request.method == "POST":
        form = NewCarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            context = {
                'form': form,
                'title': 'add new car',
                'img_obj': img_obj
            }
            return render(request, 'add_new_car.html', context)
    else:
        form = NewCarForm()
    return render(request, 'add_new_car.html',{'form':form})


class Choose_auto(TemplateView):
    model = ModelOfCar.objects.all()
    template_name = 'form_template.html'
    print(model)


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


def get_error_page(request):
    return render(request, 'error.html')