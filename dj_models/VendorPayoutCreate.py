class VendorPayoutCreate(models.Model):
    vendorPayout = models.VendorPayout()
    payoutErrors = models.PayoutError()
