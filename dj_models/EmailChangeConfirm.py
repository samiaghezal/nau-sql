class EmailChangeConfirm(models.Model):
    user = models.User()
    accountErrors = models.AccountError()

