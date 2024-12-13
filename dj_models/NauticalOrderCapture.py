class NauticalOrderCapture(models.Model):
    order = models.NauticalOrder()
    orderErrors = models.OrderError()

