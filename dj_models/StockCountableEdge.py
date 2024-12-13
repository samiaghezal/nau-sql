class StockCountableEdge(models.Model):
    node = models.Stock()
    cursor = models.String()

