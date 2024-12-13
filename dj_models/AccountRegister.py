class AccountRegister(models.Model):
    requiresConfirmation = models.Boolean()
    accountErrors = models.AccountError()
    user = models.User()

