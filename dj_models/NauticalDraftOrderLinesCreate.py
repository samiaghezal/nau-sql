class NauticalDraftOrderLinesCreate(models.Model):
    order = models.NauticalOrder()
    orderLines = models.NauticalOrderLine()
    orderErrors = models.OrderError()

