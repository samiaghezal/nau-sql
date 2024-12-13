class DashboardOrdersSummaryType(models.Model):
    filters = models.FilterObjectType()
    current = models.AbstractOrderSellerReportType()
    previous = models.AbstractOrderSellerReportType()
    deltas = models.OrderSummaryDeltaDataType()
    ordersToFulfill = models.Int()
    paymentsToProcess = models.Int()
    returnsToProcess = models.Int()
    pendingReviews = models.Int()
    pendingPayouts = models.Int()

