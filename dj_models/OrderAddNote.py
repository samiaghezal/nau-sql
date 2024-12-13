class OrderAddNote(models.Model):
    order = models.Order()
    event = models.OrderEvent()
    orderErrors = models.OrderError()

