class CheckoutSellerShipping(models.Model):
    tenant = models.Tenant()
    id = models.ID()
    seller = models.Seller()
    shippingMethod = models.ShippingMethod()
    isPriceOverridden = models.Boolean()
    priceOverrideAmount = models.Decimal()

