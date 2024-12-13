class PriceBookVariantHistory(models.Model):
    id = models.ID()
    priceBook = models.PriceBook()
    variantId = models.Int()
    valueType = models.PriceBookVariantHistoryValueType()
    currency = models.String()
    createdAt = models.Date()
    price = models.Money()
    percentage = models.Float()
    deleted = models.Boolean()

