class VariantFeature(models.Model):
    id = models.ID()
    sortOrder = models.Int()
    tenant = models.Tenant()
    featureType = models.FeatureTypeEnum()
    name = models.String()
    description = models.String()
    options = models.String()
    variant = models.ProductVariant()
    productTypeFeature = models.ProductTypeVariantFeature()

