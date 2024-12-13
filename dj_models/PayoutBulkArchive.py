class PayoutBulkArchive(models.Model):
    count = models.Int()
    payoutErrors = models.PayoutError()

