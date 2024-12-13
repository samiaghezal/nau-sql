class PriceBookVariant(models.Model):
    id = models.ID()
    priceBook = models.PriceBook()
    variant = models.ProductVariant()
    valueType = models.PriceBookVariantValueType()
    currency = models.String()
    price = models.Money()
    percentage = models.Float()

