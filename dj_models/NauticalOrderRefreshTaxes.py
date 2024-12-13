class NauticalOrderRefreshTaxes(models.Model):
    nauticalOrder = models.NauticalOrder()
    orderErrors = models.OrderError()

