class NauticalDraftOrderUpdate(models.Model):
    orderErrors = models.OrderError()
    nauticalOrder = models.NauticalOrder()

