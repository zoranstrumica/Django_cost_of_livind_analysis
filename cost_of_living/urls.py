from django.urls import path
from . import views




urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("cost_of_living/", views.cost_of_living_view, name='cost_of_living'),
    path('australia/', views.australia_data_view, name='australia_analysis'),
    path('germany/', views.germany_data_view, name='germany_analysis'),
    path('europe/', views.europe_data_view, name='europe_analysis'),
    path('asia/', views.asia_data_view, name='asia_analysis'),
    path('africa/', views.africa_data_view, name='africa_analysis'),
    path('north_america/', views.north_america_data_view, name='north_america_analysis'),
    path('south_america/', views.south_america_data_view, name='south_america_analysis'),
    path('oceania/', views.oceania_data_view, name='oceania_analysis'),
    path('grafikoni/', views.grafikoni_view, name='grafikoni'),
    path('godisni_proseci/', views.cost_of_living_by_year_view, name='godisni_proseci'),
]