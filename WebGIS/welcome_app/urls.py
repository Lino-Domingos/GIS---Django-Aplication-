from django.urls import path
from django.views import teste


urlpatterns = [
    path('minha-url/', views.teste, name='minha_view'),
    # Outras URLs do aplicativo
]

