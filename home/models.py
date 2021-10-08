from django.conf import settings
from django.db import models


class Ktiria(models.Model):
    "Generated Model"
    eidos = models.TextField()
    tetragonika = models.BigIntegerField(
        null=True,
        blank=True,
    )


class Diakstiria(models.Model):
    "Generated Model"
    fk_ktirio = models.ForeignKey(
        "home.Ktiria",
        on_delete=models.CASCADE,
        related_name="diakstiria_fk_ktirio",
    )
    eidos_dikastiriou = models.TextField(
        null=True,
        blank=True,
    )
