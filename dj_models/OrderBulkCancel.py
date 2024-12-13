class OrderBulkCancel(models.Model):
    count = models.Int()
    orderErrors = models.OrderError()

