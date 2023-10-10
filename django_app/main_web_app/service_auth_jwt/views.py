from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, BasePermission, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

# class ExampleView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, format=None):
#         content = {
#             'status': 'request was permitted'
#         }
#         return Response(content)

def get_start_page(request):
    return render(request, 'start_page.html', {'title': 'start_page'})


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(f'name={username},\n password={password}')
        user = User.objects.create_user(username=username, password=password)
        print(user)
        if user:
            login(request, user)
            messages.success(request, 'success')
            return redirect('main_page.html')
        else:
            return redirect('')
    return render(request,'registration_page.html', status=status.HTTP_201_CREATED)


def authentication(request):
    if request.method == 'POST':
        name = request.POST['username']
        password = request.POST['password']

    return render(request, 'authentication.html', status=status.HTTP_202_ACCEPTED)
