class AgreementBulkPublish(models.Model):
    count = models.Int()
    agreementErrors = models.AgreementError()

