from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import TokenObtainPairView
from .views import AuView
urlpatterns = [
    path('api/token', TokenObtainPairView.as_view(), name="token_obtain"),
    path('api/token/refresh', TokenRefreshView.as_view(), name="token_refresh"),

    path('test/',AuView.as_view())
]
