class PriceBookProductTypeBulkDelete(models.Model):
    count = models.Int()
    priceBookErrors = models.PriceBookError()

