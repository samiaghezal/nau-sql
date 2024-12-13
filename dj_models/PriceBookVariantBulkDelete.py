class PriceBookVariantBulkDelete(models.Model):
    count = models.Int()
    priceBookErrors = models.PriceBookError()

