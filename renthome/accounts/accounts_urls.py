from django.urls import path
from accounts import views

urlpatterns = [
    path('signin/',views.sign_in, name='sign-in'),
    path('signup/choose/',views.user_type, name='user-type'),
    path('signup/',views.sign_up, name='sign-up'),
]