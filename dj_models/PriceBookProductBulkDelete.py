class PriceBookProductBulkDelete(models.Model):
    count = models.Int()
    priceBookErrors = models.PriceBookError()

