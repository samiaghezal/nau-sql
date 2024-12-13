class UserPermission(models.Model):
    code = models.PermissionEnum()
    name = models.String()
    sourcePermissionGroups = models.Group()

