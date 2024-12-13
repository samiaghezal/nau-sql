class PriceBookProductHistoryCountableEdge(models.Model):
    node = models.PriceBookProductHistory()
    cursor = models.String()

