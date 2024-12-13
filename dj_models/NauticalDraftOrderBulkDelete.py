class NauticalDraftOrderBulkDelete(models.Model):
    count = models.Int()
    orderErrors = models.OrderError()

