class CustomerCreate(models.Model):
    accountErrors = models.AccountError()
    user = models.User()

