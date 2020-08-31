from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from .models import User
from django.http import HttpResponse


def login_message_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(request, "Available only to logged in users.")
            return redirect(settings.LOGIN_URL)

        return function(request, *args, **kwargs)

    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.level == '1' or request.user.level == '0':
            return function(request, *args, **kwargs)

        messages.info(request, "You do not have access rights.")
        return redirect('/users/main/')

    return wrap


def logout_message_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, "This is already an logged user.")
            return redirect('/users/main/')

        return function(request, *args, **kwargs)

    return wrap