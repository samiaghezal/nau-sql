class NauticalOrderLineBulkCancel(models.Model):
    count = models.Int()
    order = models.NauticalOrder()

