class AddressSetDefault(models.Model):
    user = models.User()
    accountErrors = models.AccountError()

