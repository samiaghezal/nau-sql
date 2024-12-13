class SingleVendorPayoutReport(models.Model):
    payouts = models.SingleVendorReportType()
    summary = models.SingleVendorSummaryType()

