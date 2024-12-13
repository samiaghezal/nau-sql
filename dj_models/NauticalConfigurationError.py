class NauticalConfigurationError(models.Model):
    field = models.String()
    message = models.String()
    code = models.NauticalConfigurationErrorCode()

