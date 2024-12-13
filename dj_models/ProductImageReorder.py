class ProductImageReorder(models.Model):
    product = models.Product()
    images = models.ProductImage()
    productErrors = models.ProductError()

