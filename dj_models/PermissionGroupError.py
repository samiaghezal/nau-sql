class PermissionGroupError(models.Model):
    field = models.String()
    message = models.String()
    code = models.PermissionGroupErrorCode()
    permissions = models.PermissionEnum()
    users = models.ID()

