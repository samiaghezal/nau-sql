class PriceBookProductTypeHistory(models.Model):
    id = models.ID()
    priceBook = models.PriceBook()
    productTypeId = models.Int()
    valueType = models.PriceBookProductTypeHistoryValueType()
    currency = models.String()
    createdAt = models.Date()
    price = models.Money()
    percentage = models.Float()
    deleted = models.Boolean()

