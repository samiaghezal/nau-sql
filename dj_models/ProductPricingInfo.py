class ProductPricingInfo(models.Model):
    onSale = models.Boolean()
    discount = models.TaxedMoney()
    discountLocalCurrency = models.TaxedMoney()
    priceRange = models.TaxedMoneyRange()
    priceRangeUndiscounted = models.TaxedMoneyRange()
    priceRangeLocalCurrency = models.TaxedMoneyRange()
    priceRangeUndiscountedLocalCurrency = models.TaxedMoneyRange()

