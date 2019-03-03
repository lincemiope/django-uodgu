from datetime import datetime
from time import time
from django.utils.timesince import timesince
from rest_framework import serializers
from uodgu.models import Guild, Member, Sop

class MemberSerializer(serializers.ModelSerializer):
    # guild = GuildSerializer()
    class Meta:
        model = Member
        exclude = ("id","api_key",)

    def validate(self, data):
        if data["username"] == data["password"]:
            raise serializers.ValidationError("Utente e password devono differire l'uno dall'altra")
        return data

    def validate_password(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("La password deve essere lunga almeno 6 caratteri")
        return value

class GuildSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)
    class Meta:
        model = Guild
        exclude = ("id",)

class SopSerializer(serializers.ModelSerializer):
    days= serializers.SerializerMethodField()
    skills_list = []
    class Meta:
        model = Sop
        exclude = ("id","expiration",)

    def get_days(self, object):
        now = datetime.now()
        expiration = object.expiration
        return (expiration - now).days

    def post_days(self, object):
        object.expiration = int(object.days * 86400 + time())

    def put_days(self, object):
        object.expiration = int(object.days * 86400 + time())

    def validate_days(self, value):
        if value < 1 or value > 90:
            raise serializers.ValidationError("I giorni devono avere un range tra 1 e 90")
        return value

    def validate_value(self, value):
        if value not in [105,110,115,120]:
            raise serializers.ValidationError("I valori possibili sono 105, 110, 115, 120")
        return value

    def validate_skill(self, value):
        if value not in self.skills_list:
            raise serializers.ValidationError(f"La skill { value } non è presente nella lista di quelle aventi sop")
        return value

# class SopSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     value = serializers.IntegerField()
#     skill = serializers.CharField(max_length=20, default='Anatomy')
#     expiration = serializers.FloatField(default=0.0)
#     serial = serializers.IntegerField(default=1)
#     guild_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Sop.objects.create(**validated_data)
