class VendorPayoutsBulkInclude(models.Model):
    count = models.Int()
    payoutErrors = models.PayoutError()

