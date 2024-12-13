class PriceBookBulkDelete(models.Model):
    count = models.Int()
    priceBookErrors = models.PriceBookError()

