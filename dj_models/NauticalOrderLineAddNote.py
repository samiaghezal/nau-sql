class NauticalOrderLineAddNote(models.Model):
    orderErrors = models.OrderError()
    nauticalOrderLine = models.NauticalOrderLine()

