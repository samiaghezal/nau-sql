class NauticalHistoricalOrderCreate(models.Model):
    orderErrors = models.OrderError()
    nauticalOrder = models.NauticalOrder()

