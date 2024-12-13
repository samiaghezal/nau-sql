class TenantError(models.Model):
    field = models.String()
    message = models.String()
    code = models.TenantErrorCode()

