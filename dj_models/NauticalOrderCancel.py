class NauticalOrderCancel(models.Model):
    order = models.NauticalOrder()
    orderErrors = models.OrderError()

