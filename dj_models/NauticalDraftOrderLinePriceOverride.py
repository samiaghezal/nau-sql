class NauticalDraftOrderLinePriceOverride(models.Model):
    nauticalOrder = models.NauticalOrder()
    orderErrors = models.OrderError()
    nauticalOrderLine = models.NauticalOrderLine()

