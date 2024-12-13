class InReportMarketplacePaymentsSummaryType(models.Model):
    category = models.String()
    title = models.String()
    columns = models.ColumnObjectType()
    filters = models.FilterObjectType()
    summary = models.AbstractPaymentsType()
    report = models.PaymentsDayReportType()

