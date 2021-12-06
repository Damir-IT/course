from django.urls import path
from .views import auth_page, base

urlpatterns = [
    path('', auth_page, name='auth_page'),
    path('course/', base, name='base'),
]