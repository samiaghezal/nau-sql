class AccountDelete(models.Model):
    accountErrors = models.AccountError()
    user = models.User()

