class NauticalOrderVoid(models.Model):
    order = models.NauticalOrder()
    orderErrors = models.OrderError()

