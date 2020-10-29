from django.db import models


# Create your models here.


class Film(models.Model):
    created = models.DateTimeField(auto_now_add=True, null=True)
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=150)

    class Meta:
        ordering = ['created']
