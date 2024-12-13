class ProductImageCountableEdge(models.Model):
    node = models.ProductImage()
    cursor = models.String()

