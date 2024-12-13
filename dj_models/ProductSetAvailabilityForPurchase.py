class ProductSetAvailabilityForPurchase(models.Model):
    product = models.Product()
    productErrors = models.ProductError()

