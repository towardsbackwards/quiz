from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import get_user_model

User = get_user_model()


class Login(LoginView):
    """Стандартная обработка входа в систему"""
    success_message = 'Вход успешно осуществлен'


class Logout(LogoutView):
    """Стандартная обработка выхода из системы"""
    success_message = 'Выход успешно осуществлен'
    url_redirect = '/'
