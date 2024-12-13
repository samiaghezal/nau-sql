class DraftOrderCreate(models.Model):
    orderErrors = models.OrderError()
    order = models.Order()

