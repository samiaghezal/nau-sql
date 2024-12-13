class AgreementUpdate(models.Model):
    agreementErrors = models.AgreementError()
    agreement = models.Agreement()

