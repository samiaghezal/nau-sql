class VerifyToken(models.Model):
    user = models.User()
    isValid = models.Boolean()
    payload = models.GenericScalar()
    accountErrors = models.AccountError()

