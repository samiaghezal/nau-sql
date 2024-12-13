class InReportMarketplacePayoutsSummaryType(models.Model):
    category = models.String()
    title = models.String()
    columns = models.ColumnObjectType()
    filters = models.FilterObjectType()
    summary = models.OrderSellerSummaryType()
    report = models.OrderSellerReportType()

