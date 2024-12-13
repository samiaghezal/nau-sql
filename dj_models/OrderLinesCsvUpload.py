class OrderLinesCsvUpload(models.Model):
    order = models.Order()
    csvFile = models.ImportFile()
    successfulLines = models.Int()
    failedLines = models.Int()
    orderErrors = models.OrderError()

