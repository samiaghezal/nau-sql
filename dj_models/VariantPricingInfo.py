class VariantPricingInfo(models.Model):
    onSale = models.Boolean()
    discount = models.TaxedMoney()
    discountLocalCurrency = models.TaxedMoney()
    price = models.TaxedMoney()
    priceUndiscounted = models.TaxedMoney()
    priceLocalCurrency = models.TaxedMoney()
    priceUndiscountedLocalCurrency = models.TaxedMoney()

