class ProductVariantCountableEdge(models.Model):
    node = models.ProductVariant()
    cursor = models.String()

