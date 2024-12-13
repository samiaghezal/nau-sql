class PriceBookProductCountableEdge(models.Model):
    node = models.PriceBookProduct()
    cursor = models.String()

