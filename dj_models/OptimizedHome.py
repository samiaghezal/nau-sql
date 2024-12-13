class OptimizedHome(models.Model):
    sales = models.TaxedMoney()
    orders = models.Int()
    toFulfill = models.Int()
    toCapture = models.Int()
    outOfStock = models.Int()
    topProducts = models.ProductVariant()
    sellerActivities = models.OrderEvent()
    marketplaceActivities = models.NauticalOrderEvent()

