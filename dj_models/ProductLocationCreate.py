class ProductLocationCreate(models.Model):
    product = models.Product()
    location = models.Location()
    productErrors = models.ProductError()

