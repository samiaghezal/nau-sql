from django.db import models

from ...core.models import PermissionEnum


class Permission(models.Model):
    code = models.CharField(
        max_length=100,
        choices=PermissionEnum.choices,
        unique=True
    )
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'permission'

    def __str__(self):
        return self.name 