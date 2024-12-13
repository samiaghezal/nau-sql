class DraftOrderLineDelete(models.Model):
    order = models.Order()
    orderLine = models.OrderLine()
    orderErrors = models.OrderError()

