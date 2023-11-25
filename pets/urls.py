from django.urls import path
from .views import PetListAPIView, PetDetailAPIView

urlpatterns = [
    path('', PetListAPIView.as_view(), name='pet-list'),
    path('<int:pk>/', PetDetailAPIView.as_view(), name='pet-detail'),
]
