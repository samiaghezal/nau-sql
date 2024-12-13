class UserAddToPriceBook(models.Model):
    user = models.User()
    priceBookErrors = models.PriceBookError()

