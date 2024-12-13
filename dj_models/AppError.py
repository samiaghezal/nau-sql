class AppError(models.Model):
    field = models.String()
    message = models.String()
    code = models.AppErrorCode()
    permissions = models.PermissionEnum()

