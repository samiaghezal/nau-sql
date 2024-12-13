class NauticalDraftOrderLineDelete(models.Model):
    order = models.NauticalOrder()
    orderLine = models.NauticalOrderLine()
    orderErrors = models.OrderError()

