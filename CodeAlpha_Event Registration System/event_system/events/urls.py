from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('events/', views.event_list, name='events'),
    path('register-event/<int:event_id>/', views.register_event, name='register_event'),
    path('myregistrations/', views.my_registrations, name='myregistrations'),
    path('cancel/<int:reg_id>/', views.cancel_registration, name='cancel_registration'),
]