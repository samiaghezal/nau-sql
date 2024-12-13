class ProductFeatureCountableEdge(models.Model):
    node = models.ProductFeature()
    cursor = models.String()

