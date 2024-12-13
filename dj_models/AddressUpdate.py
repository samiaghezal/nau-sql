class AddressUpdate(models.Model):
    user = models.User()
    accountErrors = models.AccountError()
    address = models.Address()

