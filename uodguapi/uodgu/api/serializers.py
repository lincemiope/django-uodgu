from rest_framework import serializers
from uodgu.models import Guild, Member, Sop

class GuildSerializer(serializers.Serializer):
    id = models.BigIntegerField(readonly=True)
    name = models.CharField(max_length=45)
    tapi_key = models.CharField(max_length=45, blank=True)
    tchat_id = models.CharField(max_length=45, blank=True)
    dapi_key = models.CharField(max_length=45, blank=True)
    dchat_id = models.CharField(max_length=45, blank=True)
    soplist = models.PositiveIntegerField(default=0)
    sopmanager = models.PositiveIntegerField(default=2)
    guild = models.PositiveIntegerField(default=3)
    champcount = models.PositiveIntegerField(default=2)
    raid = models.PositiveIntegerField(default=1)
    razor_key = models.CharField(readonly=True)

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
    id = models.BigIntegerField(readonly=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    alias = models.CharField(max_length=20, default='')
    rank = models.PositiveIntegerField()
    roles = models.CharField(max_length=3, default='111')
    email = models.CharField(max_length=45, default='')
    guild = models.ForeignKey(Guild,
                            on_delete=models.CASCADE,
                            related_name='members')
    creation_date = models.DateTimeField(default=1, primary_key=True))
    last_login = models.DateTimeField(default=1, primary_key=True))
    last_ip = models.CharField(readonly=True)
    api_key = models.CharField(readonly=True)

    def create(self, validated_data):
        return Member.objects.create(**validated_data)

class SopSerializer(serializers.Serializer):
    id = models.BigIntegerField(readonly=True)
    value = models.PositiveIntegerField()
    skill = models.CharField(max_length=20, default='Anatomy')
    expiration = models.FloatField(default=0.0)
    serial = models.IntegerField(default=1)
    guild = models.ForeignKey(Guild,
                            on_delete=models.CASCADE,
                            related_name='sops')

    def create(self, validated_data):
        return Sop.objects.create(**validated_data)
