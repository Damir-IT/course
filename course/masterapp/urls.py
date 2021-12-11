from django.urls import path
from .views import auth_page, base, money_intelligence, course_page, logout, logout_user


urlpatterns = [
    path('', auth_page, name='auth_page'),
    path('главная/', base, name='base'),
    path('logout', logout_user, name='logout'),
    path('денежный_интелект/', money_intelligence, name='money_intelligence'),
    path('денежный_интелект/<int:post_id>/', course_page, name='course_page'),
]
