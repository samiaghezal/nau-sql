class DraftOrderLinePriceOverride(models.Model):
    order = models.Order()
    orderErrors = models.OrderError()
    orderLine = models.OrderLine()

