class VendorPayoutReport(models.Model):
    included = models.VendorPayoutReportSubset()
    excluded = models.VendorPayoutReportSubset()

