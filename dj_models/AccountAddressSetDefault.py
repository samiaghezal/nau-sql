class AccountAddressSetDefault(models.Model):
    user = models.User()
    accountErrors = models.AccountError()

