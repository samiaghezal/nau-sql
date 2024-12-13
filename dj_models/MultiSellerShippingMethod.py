class MultiSellerShippingMethod(models.Model):
    seller = models.Int()
    sellerId = models.ID()
    sellerName = models.String()
    value = models.ShippingMethod()

