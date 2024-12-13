class PriceBookCountableEdge(models.Model):
    node = models.PriceBook()
    cursor = models.String()

