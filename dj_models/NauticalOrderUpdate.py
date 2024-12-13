class NauticalOrderUpdate(models.Model):
    orderErrors = models.OrderError()
    nauticalOrder = models.NauticalOrder()

