class DraftOrderLinesCreate(models.Model):
    order = models.Order()
    orderLines = models.OrderLine()
    orderErrors = models.OrderError()

