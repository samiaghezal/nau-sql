class NauticalOrderUpdateDeleteDiscount(models.Model):
    nauticalOrder = models.NauticalOrder()
    orderErrors = models.OrderError()

