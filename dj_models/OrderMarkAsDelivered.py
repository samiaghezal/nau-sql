class OrderMarkAsDelivered(models.Model):
    orderErrors = models.OrderError()
    order = models.Order()

