class OrderSummaryDeltaDataType(models.Model):
    percent = models.AbstractPercentReportType()
    values = models.AbstractOrderSellerReportType()

