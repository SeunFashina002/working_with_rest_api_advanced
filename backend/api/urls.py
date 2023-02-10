from django.urls import path

from .views import api_home
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns=[
    path('auth/', obtain_auth_token),
    path('', api_home, name='home'),
]