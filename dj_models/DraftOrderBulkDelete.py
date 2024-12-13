class DraftOrderBulkDelete(models.Model):
    count = models.Int()
    orderErrors = models.OrderError()

