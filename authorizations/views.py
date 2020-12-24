from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView as BaseTokenObtainPairView,
)
from .serializers import TokenObtainPairSerializer


class TokenObtainPairView(BaseTokenObtainPairView):
    serializer_class = TokenObtainPairSerializer


class AuView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({'key': 'proverka'})