class AuthError(models.Model):
    field = models.String()
    message = models.String()
    code = models.String()

