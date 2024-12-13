class PriceBookProductTypeCountableEdge(models.Model):
    node = models.PriceBookProductType()
    cursor = models.String()

