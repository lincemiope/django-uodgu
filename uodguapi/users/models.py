from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Guild(models.Model):
    name = models.CharField(max_length=45)
    tag = models.CharField(max_length=10)
    tapi_key = models.CharField(max_length=45, blank=True)
    tchat_id = models.CharField(max_length=45, blank=True)
    dapi_key = models.CharField(max_length=45, blank=True)
    dchat_id = models.CharField(max_length=45, blank=True)

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    alias = models.CharField(max_length=45)
    rank = models.PositiveIntegerField(default=0)
    roles = models.CharField(max_length=3, default='000')

    guild = models.ForeignKey(Guild,
                            on_delete=models.CASCADE,
                            related_name='members',
                            null=True)

    class Meta:
        permissions = (
            ('can_see_sops','Può vedere le sop'),
            ('can_add_sops','Può aggiungere sop'),
            ('can_del_sops','Può cancellare sop'),
            ('can_see_champs','Può vedere i champ'),
            ('can_add_champs','Può aggiungere champ'),
            ('can_edit_champs','Può modificare i champ'),
            ('can_del_champs','Può cancellare champ'),
            ('can_see_guild','Può vedere le impostazioni di gilda'),
            ('can_edit_guild','Può modificare le impostazioni di gilda'),
            ('can_see_members','Può vedere i dati dei membri'),
            ('can_add_members','Può aggiungere membri'),
            ('can_edit_members','Può modificare i membri'),
            ('can_del_members','Può cancellare i membri'),
            ('can_see_requests','Può vedere le richieste'),
            ('can_add_request','Può richiedere una sop'),
            ('can_add_requests','Può aggiungere richieste altrui'),
            ('can_del_requests','Può rimuovere richieste altrui'),
            ('is_guildmaster','È guildmaster')
        )
