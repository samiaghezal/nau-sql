class AuthURLGenerate(models.Model):
    authUrl = models.String()
    accountErrors = models.AccountError()

