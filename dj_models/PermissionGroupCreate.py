class PermissionGroupCreate(models.Model):
    permissionGroupErrors = models.PermissionGroupError()
    group = models.Group()

