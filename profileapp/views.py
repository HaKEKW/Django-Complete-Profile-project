import joblib
import numpy
import pandas as pd
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .decorators import unauthenticated_user
from .forms import CreateUserForm, ProfileForm, ResultForm
from .models import PredictedModel


# Create your views here.

@login_required(login_url='login')
def index(request):
    obj = PredictedModel.objects.filter(profile=request.user.profile)
    context = {'obj': obj}
    return render(request, 'profileapp/home.html', context)


@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            return redirect('/')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form': form}
    return render(request, 'profileapp/profile.html', context)


@login_required(login_url='predict')
def predictions(request):
    if request.method == 'POST':
        form = ResultForm(request.POST)
        if form.is_valid():
            new_obj = form.save()
            form_data = request.POST.dict()

            print(form_data)
            # data = pd.DataFrame(
            #     {'OpenDays': [numpy.int64(int(form_data['open_days']))],
            #      'Big Cities': form_data['big_cities'], 'Other': not form_data['big_cities'],
            #      'P2': form_data['P2'], 'P8': form_data['P8'], 'P22': form_data['P22'],
            #      'P24': form_data['P24'], 'P28': form_data['P28'], 'P26': form_data['P26']})
            # model = joblib.load("/Users/hak/PycharmProjects/Django-Complete-Profile-project/random_forest.joblib")
            # predicted_results = model.predict(data)
            # print(predicted_results)
            new_obj.profile = request.user.profile
            # new_obj.results = str(predicted_results[0])
            new_obj.results = 2
            new_obj.save()
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
