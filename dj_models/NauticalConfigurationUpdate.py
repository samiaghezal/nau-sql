class NauticalConfigurationUpdate(models.Model):
    nauticalConfigurationList = models.NauticalConfiguration()
    nauticalConfigurationErrors = models.NauticalConfigurationError()

