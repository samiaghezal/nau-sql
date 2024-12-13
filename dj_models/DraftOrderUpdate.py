class DraftOrderUpdate(models.Model):
    orderErrors = models.OrderError()
    order = models.Order()

