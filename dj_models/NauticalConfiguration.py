class NauticalConfiguration(models.Model):
    configurationName = models.String()
    configurationValue = models.Boolean()
    configurationValueDatetime = models.DateTime()
    configurationValueString = models.String()

