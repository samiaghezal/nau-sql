class RefreshToken(models.Model):
    token = models.String()
    user = models.User()
    accountErrors = models.AccountError()

