class PasswordSet(models.Model):
    token = models.String()
    refreshToken = models.String()
    csrfToken = models.String()
    user = models.User()
    accountErrors = models.AccountError()

