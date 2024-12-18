class TaxCertificate(models.Model):
    id = models.Int()
    companyId = models.String()
    signedDate = models.String()
    expirationDate = models.String()
    filename = models.String()
    documentExists = models.Boolean()
    downloadUrl = models.String()
    valid = models.Boolean()
    verified = models.Boolean()
    exemptPercentage = models.String()
    isSingleCertificate = models.Boolean()
    exemptionNumber = models.String()
    exemptionReasonName = models.String()
    exemptionReasonId = models.Int()
    status = models.String()
    createdDate = models.String()
    modifiedDate = models.String()
    taxNumberType = models.String()
    businessNumberType = models.String()
    exposureZoneName = models.String()

