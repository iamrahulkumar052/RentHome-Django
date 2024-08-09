from django.urls import path
from renters import views

urlpatterns = [
    path('',views.welcome_page, name='welcome'),

]