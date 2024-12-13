class CustomerUpdate(models.Model):
    accountErrors = models.AccountError()
    user = models.User()

