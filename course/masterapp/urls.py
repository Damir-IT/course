from django.urls import path
from .views import auth_page, base, logout, logout_user

urlpatterns = [
    path('', auth_page, name='auth_page'),
    path('logout', logout_user, name='logout'),
    
    path('course/', base, name='base'),
    
]