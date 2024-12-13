class VendorPayoutsBulkExclude(models.Model):
    count = models.Int()
    payoutErrors = models.PayoutError()

