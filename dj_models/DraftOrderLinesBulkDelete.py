class DraftOrderLinesBulkDelete(models.Model):
    count = models.Int()
    orderErrors = models.OrderError()

