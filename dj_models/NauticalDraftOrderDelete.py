class NauticalDraftOrderDelete(models.Model):
    orderErrors = models.OrderError()
    nauticalOrder = models.NauticalOrder()

