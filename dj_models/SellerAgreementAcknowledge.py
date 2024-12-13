class SellerAgreementAcknowledge(models.Model):
    user = models.User()
    agreementErrors = models.AgreementError()

