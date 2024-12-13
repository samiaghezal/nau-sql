class Stock(models.Model):
    warehouse = models.Warehouse()
    productVariant = models.ProductVariant()
    quantity = models.Int()
    outOfStockThreshold = models.Int()
    quantityAllocated = models.Int()
    id = models.ID()
    quantityAvailable = models.Int()

