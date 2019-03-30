from django.shortcuts import get_object_or_404

from rest_framework import generics, status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.api.serializers import UserDisplaySerializer
from users.models import CustomUser

class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)

    def put(self, request, pk):
        updating = get_object_or_404(CustomUser, pk=pk)
        user = self.request.user
        if updating.username == user.username:
            updating.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(updating, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)
