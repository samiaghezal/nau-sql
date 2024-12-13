class AccountError(models.Model):
    field = models.String()
    message = models.String()
    code = models.AccountErrorCode()

