
from django.urls import path
from Reception import views

urlpatterns =[
    path('form', views.home_view),
    path('Appointment', views.Snippet_detail),

]