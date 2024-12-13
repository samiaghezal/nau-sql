class NauticalOrderUpdateShipping(models.Model):
    order = models.NauticalOrder()
    orderErrors = models.OrderError()

