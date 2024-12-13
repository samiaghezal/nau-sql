class VendorPayoutReportSubset(models.Model):
    category = models.String()
    columns = models.ColumnObjectType()
    filters = models.FilterObjectType()
    summary = models.OrderVendorSummaryType()
    report = models.OrderVendorReportType()
    title = models.String()

