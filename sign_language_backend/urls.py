from django.urls import path, include
from rest_framework import routers
from .views import GestureViewSet
from . import views
router = routers.DefaultRouter()
router.register(r'gestures', GestureViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('detect-gesture/', views.detect_gesture, name='detect_gesture'),
    
]
