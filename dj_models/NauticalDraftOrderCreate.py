class NauticalDraftOrderCreate(models.Model):
    orderErrors = models.OrderError()
    nauticalOrder = models.NauticalOrder()

