class PriceBookVariantCountableEdge(models.Model):
    node = models.PriceBookVariant()
    cursor = models.String()

