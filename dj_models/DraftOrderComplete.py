class DraftOrderComplete(models.Model):
    order = models.Order()
    orderErrors = models.OrderError()

