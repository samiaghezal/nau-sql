class ProductImageDelete(models.Model):
    product = models.Product()
    image = models.ProductImage()
    productErrors = models.ProductError()

