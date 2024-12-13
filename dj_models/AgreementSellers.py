class AgreementSellers(models.Model):
    id = models.ID()
    tenant = models.Tenant()
    seller = models.Seller()
    acknowledgedOn = models.DateTime()
    plan = models.Agreement()
    effectiveAt = models.DateTime()
    privateMetadata = models.MetadataItem()
    metadata = models.MetadataItem()

