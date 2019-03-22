from django.db import models
from users.models import Guild

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
