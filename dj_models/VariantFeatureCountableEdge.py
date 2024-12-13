class VariantFeatureCountableEdge(models.Model):
    node = models.VariantFeature()
    cursor = models.String()

