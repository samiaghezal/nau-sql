class OrderPayoutStatusUpdate(models.Model):
    order = models.Order()
    orderErrors = models.OrderError()

