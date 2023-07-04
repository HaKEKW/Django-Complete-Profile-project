import logging
from io import BytesIO

import joblib
import numpy
import pandas as pd
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import FileResponse
from django.shortcuts import render
from reportlab.pdfgen import canvas
import json
from django.forms.models import model_to_dict

from .decorators import unauthenticated_user
from .forms import CreateUserForm, ProfileForm, ResultForm
from .models import PredictedModel
from .logic import find_random_value

logger = logging.getLogger('views.py')


@login_required(login_url='login')
def index(request):
    obj = PredictedModel.objects.filter(profile=request.user.profile)
    latest_obj = PredictedModel.objects.last()
    context = {'obj': obj, 'latest_obj': latest_obj}
    return render(request, 'profileapp/home.html', context)


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            logger.info('Обновленные даннык сохранена успешно', request.path, username)
            return redirect('/')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form': form}
    return render(request, 'profileapp/profile.html', context)


@login_required(login_url='login')
def predictions(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            new_obj = form.save()
            new_obj.profile = request.user.profile
            # new_obj.results = str(predicted_results[0])
            new_obj.results = find_random_value('train.csv')
            new_obj.save()
            logger.info('Форма заполнена успешно, данные подсчитаны', request.path)
            return redirect('/')
    else:
        form = ResultForm(request.POST)
    context = {'form': form}
    return render(request, 'profileapp/predict_table.html', context)


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect("/")
        else:
            messages.info(request, 'Wrong passwrod or username')
            return redirect('login')
    return render(request, 'profileapp/login_page.html')


@unauthenticated_user
def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            return redirect('login')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'profileapp/register_page.html', context)

    context = {'form': form}
    return render(request, 'profileapp/register_page.html', context)


@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('login')


@login_required(login_url='login')
def download_pdf(request):
    data = model_to_dict(PredictedModel.objects.last())
    buffer = BytesIO()

    pdf = canvas.Canvas(buffer)
    y = 800
    for key, value in data.items():
        text = f"{key}: {value}"
        pdf.drawString(50, y, text)
        y -= 20
    # pdf.showPage()
    pdf.save()
    buffer.seek(0)
    response = FileResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'
    return response
