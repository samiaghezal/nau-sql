class StaffError(models.Model):
    field = models.String()
    message = models.String()
    code = models.AccountErrorCode()
    permissions = models.PermissionEnum()
    groups = models.ID()
    users = models.ID()

