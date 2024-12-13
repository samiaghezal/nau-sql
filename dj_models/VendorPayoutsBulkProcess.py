class VendorPayoutsBulkProcess(models.Model):
    count = models.Int()
    payoutErrors = models.PayoutError()

