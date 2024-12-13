class AgreementError(models.Model):
    field = models.String()
    message = models.String()
    code = models.AgreementErrorCode()

