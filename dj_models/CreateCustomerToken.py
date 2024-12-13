class CreateCustomerToken(models.Model):
    nauticalToken = models.String()
    refreshToken = models.String()
    authErrors = models.AuthError()

