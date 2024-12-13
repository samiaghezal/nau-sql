class VendorPayoutStatusUpdate(models.Model):
    vendorPayout = models.VendorPayout()
    payoutErrors = models.PayoutError()

