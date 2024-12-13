class ValidationStatus(models.Model):
    message = models.String()
    code = models.String()
    variant = models.ID()

