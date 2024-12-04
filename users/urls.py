from django.urls import path
from . import views




urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('my_profile/', views.my_profile, name='my_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('contact/', views.contact, name='contact'),
    path('all_contacts/', views.all_contacts, name='all_contacts'),
]