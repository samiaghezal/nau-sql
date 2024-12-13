class AgreementCommission(models.Model):
    id = models.ID()
    tenant = models.Tenant()
    commission = models.Decimal()
    agreement = models.Agreement()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()
    instance = models.Category()

