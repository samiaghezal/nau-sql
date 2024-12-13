class EmailChangeRequest(models.Model):
    user = models.User()
    accountErrors = models.AccountError()

