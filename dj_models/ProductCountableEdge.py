class ProductCountableEdge(models.Model):
    node = models.Product()
    cursor = models.String()

