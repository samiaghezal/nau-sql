class SellerAgreementDecline(models.Model):
    user = models.User()
    agreementErrors = models.AgreementError()

