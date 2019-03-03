from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from uodgu.models import Guild, Member, Sop
from uodgu.api.serializers import GuildSerializer, MemberSerializer, SopSerializer
