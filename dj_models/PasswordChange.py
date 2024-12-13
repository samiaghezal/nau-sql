class PasswordChange(models.Model):
    user = models.User()
    accountErrors = models.AccountError()

