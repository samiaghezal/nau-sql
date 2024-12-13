class ProductTypeCountableEdge(models.Model):
    node = models.ProductType()
    cursor = models.String()

