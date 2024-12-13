class NauticalOrderUpdateMarketplaceShipping(models.Model):
    order = models.NauticalOrder()
    orderErrors = models.OrderError()

