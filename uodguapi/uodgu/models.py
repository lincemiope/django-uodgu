from django.db import models

class Guild(models.Model):
    # id = models.BigIntegerField(default=1, primary_key=True)
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
    razor_key = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return self.name

class Sop(models.Model):
    # id = models.BigIntegerField(default=1, primary_key=True)
    value = models.PositiveIntegerField()
    skill = models.CharField(max_length=20, default='Anatomy')
    expiration = models.FloatField(default=0.0)
    serial = models.IntegerField(default=1)
    guild = models.ForeignKey(Guild,
                            on_delete=models.CASCADE,
                            related_name='sops')

    def __str__(self):
        return self.value + ' ' + self.skill

class Member(models.Model):
    # id = models.BigIntegerField(default=1, primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    alias = models.CharField(max_length=20, default='')
    rank = models.PositiveIntegerField()
    roles = models.CharField(max_length=3, default='111')
    email = models.CharField(max_length=45, default='')
    guild = models.ForeignKey(Guild,
                            on_delete=models.CASCADE,
                            related_name='members')
    creation_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    last_ip = models.CharField(max_length=11, default='', blank=True)
    api_key = models.CharField(max_length=64, default='', blank=True)

    def __str__(self):
        return self.username
