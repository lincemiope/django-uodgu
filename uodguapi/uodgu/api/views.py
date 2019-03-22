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

# class MemberListCreateAPIView(APIView):
#     def get(self, request):
#         members = Member.objects.all()
#         serializer = MemberSerializer(members, many=True)
#         return Response(serializer.data)

# @api_view(["GET"])
# def sop_list_view(request, pk):
#     if request.method == 'GET':
#         try:
#             sops = Sop.objects.filter(guild_id=pk)
#             serializer = SopSerializer(sops, many=True)
#             return Response(serializer.data)
#         except Sop.DoesNotExist:
#             return Response({ "error": {
#                                 "code": 404,
#                                 "message": "Nessuna sop trovata"
#             }}, status=status.HTTP_404_NOT_FOUND)
#     return Response({ "error": {
#                         "code": 405,
#                         "messaggio": "Questa API è utilizzabile solo in GET"
#     }}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#
# @api_view(["POST"])
# def sop_add(request):
#     pass
#
# @api_view(["DELETE"])
# def sop_delete(request, pk):
#     pass
