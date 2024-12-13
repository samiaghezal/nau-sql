class OrderCancel(models.Model):
    order = models.Order()
    orderErrors = models.OrderError()

