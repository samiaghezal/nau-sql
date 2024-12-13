class PriceBookVariantHistoryCountableEdge(models.Model):
    node = models.PriceBookVariantHistory()
    cursor = models.String()

