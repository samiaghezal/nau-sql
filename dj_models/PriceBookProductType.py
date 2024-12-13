class PriceBookProductType(models.Model):
    id = models.ID()
    priceBook = models.PriceBook()
    productType = models.ProductType()
    valueType = models.PriceBookProductTypeValueType()
    currency = models.String()
    price = models.Money()
    percentage = models.Float()

