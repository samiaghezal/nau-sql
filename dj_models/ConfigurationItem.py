class ConfigurationItem(models.Model):
    name = models.String()
    value = models.String()
    type = models.ConfigurationTypeFieldEnum()
    helpText = models.String()
    label = models.String()
    options = models.String()

