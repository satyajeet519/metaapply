from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response({"error": "Refresh token missing"}, status=400)

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()

        except Exception:
            # Even if token is invalid or already blacklisted, logout should still succeed
            pass

        return Response({"detail": "Logged out successfully"}, status=200)
