class AbstractProductVariantType(models.Model):
    totals = models.Int()
    grossRevenue = models.Float()
    quantityOrdered = models.Int()
    avgPriceGrossAmount = models.Float()
    maxPriceGrossAmount = models.Float()
    minPriceGrossAmount = models.Float()
    revenue = models.Float()
    avgPrice = models.Float()
    maxPrice = models.Float()
    minPrice = models.Float()

