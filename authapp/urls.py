from authapp.views import Login, Logout
from django.urls import path

app_name = 'accounts'


urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(next_page='/'), name='logout'),
]