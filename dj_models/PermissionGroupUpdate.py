class PermissionGroupUpdate(models.Model):
    permissionGroupErrors = models.PermissionGroupError()
    group = models.Group()

