class PriceBookProduct(models.Model):
    id = models.ID()
    priceBook = models.PriceBook()
    product = models.Product()
    valueType = models.PriceBookProductValueType()
    currency = models.String()
    price = models.Money()
    percentage = models.Float()

