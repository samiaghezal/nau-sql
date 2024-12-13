class Permission(models.Model):
    code = models.PermissionEnum()
    name = models.String()

