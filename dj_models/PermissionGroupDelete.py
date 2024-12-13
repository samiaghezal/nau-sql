class PermissionGroupDelete(models.Model):
    permissionGroupErrors = models.PermissionGroupError()
    group = models.Group()

