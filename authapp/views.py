from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib.auth import get_user_model

User = get_user_model()


class Login(LoginView):
    success_message = 'Вход успешно осуществлен'


class Logout(LogoutView):
    success_message = 'Выход успешно осуществлен'
    url_redirect = '/'

