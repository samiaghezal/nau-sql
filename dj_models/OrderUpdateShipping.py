class OrderUpdateShipping(models.Model):
    order = models.Order()
    orderErrors = models.OrderError()

