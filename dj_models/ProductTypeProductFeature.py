class ProductTypeProductFeature(models.Model):
    id = models.ID()
    sortOrder = models.Int()
    tenant = models.Tenant()
    featureType = models.FeatureTypeEnum()
    name = models.String()
    description = models.String()
    options = models.String()
    productType = models.ProductType()
    productFeatures = models.ProductFeatureCountableConnection()

