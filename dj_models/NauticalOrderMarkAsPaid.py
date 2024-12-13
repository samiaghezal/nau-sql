class NauticalOrderMarkAsPaid(models.Model):
    order = models.NauticalOrder()
    orderErrors = models.OrderError()

