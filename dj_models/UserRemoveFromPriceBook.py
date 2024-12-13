class UserRemoveFromPriceBook(models.Model):
    user = models.User()
    priceBookErrors = models.PriceBookError()

