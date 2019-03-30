import time
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from uodgu.models import Sop
from uodgu.api.serializers import SopSerializer

# class GuildListCreateAPIView(APIView):
#     def get(self, request):
#         guilds = Guild.objects.all()
#         serializer = GuildSerializer(guilds, many=True)
#         return Response(serializer.data)

class SopListCreateAPIView(APIView):
    def get(self, request):
        sops = Sop.objects.all()
        serializer = SopSerializer(sops, many=True)
        return Response(serializer.data)
