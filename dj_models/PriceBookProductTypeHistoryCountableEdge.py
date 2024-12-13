class PriceBookProductTypeHistoryCountableEdge(models.Model):
    node = models.PriceBookProductTypeHistory()
    cursor = models.String()

