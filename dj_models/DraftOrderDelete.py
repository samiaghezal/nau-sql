class DraftOrderDelete(models.Model):
    orderErrors = models.OrderError()
    order = models.Order()

