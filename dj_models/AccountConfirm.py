class AccountConfirm(models.Model):
    user = models.User()
    accountErrors = models.AccountError()

