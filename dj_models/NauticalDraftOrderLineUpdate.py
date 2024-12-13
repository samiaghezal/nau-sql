class NauticalDraftOrderLineUpdate(models.Model):
    order = models.NauticalOrder()
    orderErrors = models.OrderError()
    nauticalOrderLine = models.NauticalOrderLine()

