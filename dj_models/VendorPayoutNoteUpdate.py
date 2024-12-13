class VendorPayoutNoteUpdate(models.Model):
    vendorPayout = models.VendorPayout()
    event = models.VendorPayoutEvent()
    payoutErrors = models.PayoutError()

