from rest_framework import serializers
from uodgu.models import Guild, Member, Sop

class GuildSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=45)
    tapi_key = serializers.CharField(max_length=45)
    tchat_id = serializers.CharField(max_length=45)
    dapi_key = serializers.CharField(max_length=45)
    dchat_id = serializers.CharField(max_length=45)
    soplist = serializers.IntegerField(default=0)
    sopmanager = serializers.IntegerField(default=2)
    guild = serializers.IntegerField(default=3)
    champcount = serializers.IntegerField(default=2)
    raid = serializers.IntegerField(default=1)
    razor_key = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Guild.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.tapi_key = validated_data.get('tapi_key', instance.tapi_key)
        instance.tchat_id = validated_data.get('tchat_id', instance.tchat_id)
        instance.dapi_key = validated_data.get('dapi_key', instance.dapi_key)
        instance.dchat_id = validated_data.get('dchat_id', instance.dchat_id)
        instance.soplist = validated_data.get('soplist', instance.soplist)
        instance.sopmanager = validated_data.get('sopmanager', instance.sopmanager)
        instance.guild = validated_data.get('guild', instance.guild)
        instance.champcount = validated_data.get('champcount', instance.champcount)
        instance.raid = validated_data.get('raid', instance.raid)

class MemberSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)
    alias = serializers.CharField(max_length=20, default='')
    rank = serializers.IntegerField()
    roles = serializers.CharField(max_length=3, default='111')
    email = serializers.CharField(max_length=45, default='')
    guild_id = serializers.IntegerField()
    creation_date = serializers.DateTimeField(read_only=True)
    last_login = serializers.DateTimeField(read_only=True)
    last_ip = serializers.CharField(read_only=True)
    api_key = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

class SopSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    value = serializers.IntegerField()
    skill = serializers.CharField(max_length=20, default='Anatomy')
    expiration = serializers.FloatField(default=0.0)
    serial = serializers.IntegerField(default=1)
    guild_id = serializers.IntegerField()

    def create(self, validated_data):
        return Sop.objects.create(**validated_data)
