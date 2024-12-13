class ProductReorderVariants(models.Model):
    product = models.Product()
    productErrors = models.ProductError()

