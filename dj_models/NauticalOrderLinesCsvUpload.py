class NauticalOrderLinesCsvUpload(models.Model):
    nauticalOrder = models.NauticalOrder()
    csvFile = models.ImportFile()
    successfulLines = models.Int()
    failedLines = models.Int()
    orderErrors = models.OrderError()

