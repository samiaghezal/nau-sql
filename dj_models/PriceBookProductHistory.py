class PriceBookProductHistory(models.Model):
    id = models.ID()
    priceBook = models.PriceBook()
    productId = models.Int()
    valueType = models.PriceBookProductHistoryValueType()
    currency = models.String()
    createdAt = models.Date()
    price = models.Money()
    percentage = models.Float()
    deleted = models.Boolean()

