class AccountAddressDelete(models.Model):
    user = models.User()
    accountErrors = models.AccountError()
    address = models.Address()

