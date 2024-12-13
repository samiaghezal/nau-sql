class OrderError(models.Model):
    field = models.String()
    message = models.String()
    code = models.OrderErrorCode()
    warehouse = models.ID()
    orderLine = models.ID()
    variant = models.ID()

