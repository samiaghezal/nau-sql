class MenuError(models.Model):
    field = models.String()
    message = models.String()
    code = models.MenuErrorCode()

