class PriceBookUpdate(models.Model):
    priceBookErrors = models.PriceBookError()
    priceBook = models.PriceBook()

