class NauticalOrderReturnFromStorefrontNotification(models.Model):
    order = models.NauticalOrder()
    event = models.NauticalOrderEvent()
    orderErrors = models.OrderError()

