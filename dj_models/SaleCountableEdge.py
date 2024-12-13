class SaleCountableEdge(models.Model):
    node = models.Sale()
    cursor = models.String()

