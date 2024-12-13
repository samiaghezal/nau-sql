class AgreementBulkDelete(models.Model):
    count = models.Int()
    agreementErrors = models.AgreementError()

